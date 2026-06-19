from aisuite import Agent, Runner

AGENT_INSTRUCTIONS = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches. First perform search, analyze the results 
and then perform more searches. 

The question has to be about the course or its logistics, offtopic questions 
shouldn't be answered. If the search returns nothing, it's likely an off-topic question.
If you can't answer the question using FAQ, don't do it yourself. Only use the 
facts from the FAQ database.

At the end, ask if there are other areas that the user wants to explore.
""".strip()

NAIVE_RAG_INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

NAIVE_RAG_PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()


class RAGBase:
    def __init__(
        self,
        index,
        llm_client,
        # instructions=AGENT_INSTRUCTIONS,
        course="llm-zoomcamp",
        model="ollama:llama3.1:8b-instruct-q4_K_M",
    ):
        self.index = index
        self.llm_client = llm_client
        # self.instructions = instructions
        self.course = course
        self.model = model
        self.number_of_searches_called = 0

    def search(self, query: str) -> str:
        """
        Search the FAQ database for entries matching the given query.

        Args:
            query (str): The given query to look up.
        """

        self.number_of_searches_called = self.number_of_searches_called + 1
        boost_dict = {"question": 3.0, "section": 0.5}
        filter_dict = {"course": self.course}

        raw_results = self.index.search(
            query,
            num_results=5,
            boost_dict=boost_dict,
            filter_dict=filter_dict,
        )
        return raw_results

        """ lines = []
        for doc in raw_results:
            lines.append(f"Section: {doc.get('section', 'N/A')}")
            lines.append(f"Q: {doc.get('question', '')}")
            lines.append(f"A: {doc.get('answer', '')}")
            lines.append("")

        context_string = "\n".join(lines).strip()

        # 3. Fallback if no matching rows are found
        if not context_string:
            return "No matching FAQ entries found for this query database search."

        return context_string """

    def agent_rag(self, query, max_turns=10):
        """
        Executes the pipeline using aisuite's Agent and Runner engine.
        """

        self.number_of_searches_called = 0

        # Define the agent with the tools directly attached
        rag_agent = Agent(
            name="rag-assistant",
            model=self.model,
            instructions=AGENT_INSTRUCTIONS,
            tools=[self.search],
        )

        # The Runner orchestrates execution turns across problematic model drivers cleanly
        result = Runner.run_sync(agent=rag_agent, input=query, max_turns=max_turns)
        self.print_token_usage_agent(result)

        ("--- Agent Search Metric ---")
        print("Number of Searches:", self.number_of_searches_called)

        return result.final_output

    def print_token_usage_agent(self, result):
        """
        Extract raw provider response blocks out of the result object
        """
        try:
            # Captures usage dictionaries sent back from your model provider (e.g., Ollama/Groq)
            raw_history = getattr(result, "intermediate_messages", [])

            # The final response block contains the total aggregated token summary
            final_usage = raw_history[-1].get("usage", {})

            print("--- Token Usage Metric ---")
            print(f"Prompt Tokens:     {final_usage.get('prompt_tokens', 0)}")
            print(f"Completion Tokens: {final_usage.get('completion_tokens', 0)}")
            print(f"Total Tokens:      {final_usage.get('total_tokens', 0)}")
            print("--------------------------")
        except Exception:
            print(
                "[INFO] Token usage structure unavailable for this specific provider."
            )

    def naive_rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer

    def build_context(self, search_results):
        lines = []
        for doc in search_results:
            lines.append("filename: " + doc["filename"])
            lines.append("content: " + doc["content"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return NAIVE_RAG_PROMPT_TEMPLATE.format(question=query, context=context)

    def llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": NAIVE_RAG_INSTRUCTIONS},
            {"role": "user", "content": prompt},
        ]

        response = self.llm_client.responses.create(
            model=self.model, input=input_messages
        )

        self.print_token_usage_naive(response)

        return response.output_text

    def print_token_usage_naive(self, response):
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        print("--- Token Usage Metric ---")
        print(f"Prompt Tokens:     {input_tokens}")
        print(f"Completion Tokens: {output_tokens}")
        print(f"Total Tokens:      {input_tokens + output_tokens}")
        print("--------------------------")
