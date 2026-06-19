# LLM Zoomcamp 2026 - Agentic RAG Homework

## Project Overview

This project implements an Agentic RAG (Retrieval Augmented Generation) system as part of the LLM Zoomcamp 2026 homework. It demonstrates key concepts in building intelligent agents that can interact with external tools and augment their responses with retrieved information.

## Functionality

The core functionality of this project includes:
-   **Agentic RAG Implementation**: Demonstrates how to build an agent that leverages external tools for information retrieval and uses a Large Language Model (LLM) to generate informed responses.
-   **Local LLM Integration**: Focuses on the usage of local LLMs via Ollama, providing a self-contained environment for experimentation and development without relying on external API services for model inference.
-   **Tool Usage**: Incorporates the concept of agents using search tools to gather relevant context before generating responses.

## Design

The design of this project follows an agentic approach, where an LLM acts as an orchestrator, deciding when and how to use various tools to fulfill user queries. Key aspects of the design include:
-   **Modular Components**: Separation of concerns between the LLM interaction, tool definitions, and data retrieval mechanisms.
-   **Search Tool Integration**: The agent is designed to intelligently utilize a search tool (as described in the lesson materials) to retrieve pertinent information.

## Installation and Running

To set up and run this project, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/DataTalksClub/llm-zoomcamp.git
    cd llm-zoomcamp/homeworks
    ```

2.  **Install dependencies**:
    Ensure you have Python 3.9+ and `pip` installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `requirements.txt` is assumed to exist. If not, create one with necessary libraries like `ollama`, `openai`, `langchain`, etc.)

3.  **Set up Ollama (for local models)**:
    Download and install Ollama from [ollama.com](https://ollama.com/).
    Pull the required local LLM (e.g., `llama2`):
    ```bash
    ollama pull llama2
    ```

4.  **Run the notebook**:
    Start a Jupyter Notebook or Jupyter Lab server and open the relevant notebook (e.g., `naive_rag.ipynb` or `agent_rag.ipynb`).
    ```bash
    jupyter notebook
    ```
    Follow the instructions within the notebook to execute the code cells.

## Data Acquisition

To obtain the necessary data for this project, please refer to the following link:
[LLM Zoomcamp 2026 - 01-agentic-rag Homework Data](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/01-agentic-rag/homework.md)

Download or follow the instructions provided there to set up your data.

## Model Usage

### Using Ollama Local Models

This project primarily demonstrates the usage of local LLMs through Ollama. The notebooks are configured to interact with your locally running Ollama instance. Ensure Ollama is running and the desired model (e.g., `llama2`) is pulled before execution.

### Switching to OpenAI Models

To switch from Ollama local models to OpenAI models in the `naive_rag` notebook, you will typically need to:

1.  **Install OpenAI library**:
    ```bash
    pip install openai
    ```
2.  **Set your OpenAI API key**:
    Set the `OPENAI_API_KEY` environment variable or directly within your notebook:
    ```python
    import os
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    ```
3.  **Modify LLM initialization**:
    Change the LLM initialization code to use OpenAI's client. For example, if using LangChain, you would change `Ollama(model="llama2")` to `ChatOpenAI(model="gpt-4o")` or similar, depending on the specific integration.

## Agent API Usage (AISuite Agent API)

For the agentic RAG implementation utilizing aisuite Agent API, a brief description of how the search tool needs to be implemented is as follows:

The agent, when using the aisuite Agent API, requires a clear definition of the tools it can access. Specifically, the search tool integration should follow the patterns outlined in the official lesson materials. Refer to:
[LLM Zoomcamp 2026 - 01-agentic-rag Lessons](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag/lessons)

The implementation typically involves:
1.  **Defining the Search Tool**: Creating a tool object that encapsulates the logic for performing a search operation (e.g., querying a vector database, a web search engine, or a local document store).
2.  **Registering the Tool with the Agent**: Making the defined search tool available to the agent through the aisuite Agent API's tool registration mechanism.
3.  **Agent Prompting**: Crafting prompts that guide the agent to understand when to invoke the search tool and how to utilize its output to formulate a comprehensive response.

The lessons linked above provide detailed examples and code snippets for implementing these steps effectively.
