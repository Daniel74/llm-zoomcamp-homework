# LLM Zoomcamp 2026 - Agentic RAG Homework

## Project Overview

This project implements an Agentic RAG (Retrieval Augmented Generation) system as part of the LLM Zoomcamp 2026 homework. It demonstrates key concepts in building intelligent agents that can interact with external tools and augment their responses with retrieved information.

## Functionality

The core functionality of this project includes:

- **Naive and Agentic RAG Implementation**: Demonstrates how to build a naive RAG and agent RAG that leverages external tools for information retrieval and uses a Large Language Model (LLM) to generate informed responses.
- **Local LLM Integration**: Focuses on the usage of local LLMs via Ollama, providing a self-contained environment for experimentation and development without relying on external API services for model inference.
- **Tool Usage**: Incorporates the concept of agents using search tools to gather relevant context before generating responses.

## Installation and Running

To set up and run this project, follow these steps:

1.  **Clone the repository**:

    ```bash
    git clone git@github.com:Daniel74/llm-zoomcamp-homework.git
    cd llm-zoomcamp/homeworks
    ```

2.  **Install dependencies**:
    Ensure you have Python 3.13 and `pip` installed. Then, install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Ollama (for local models)**:
    Download and install Ollama from [ollama.com](https://ollama.com/).
    Pull the required local LLM (e.g., `llama2`):

    ```bash
    ollama pull llama2
    ```

4.  **Run the notebook**:

## Data Acquisition

To obtain the necessary data for this project, please refer to the following link:
[LLM Zoomcamp 2026 - 01-agentic-rag Homework Data](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/01-agentic-rag/homework.md)

Download or follow the instructions provided there to set up your data.

## Model Usage

### Using Ollama Local Models

This project primarily demonstrates the usage of local LLMs through Ollama. The notebooks are configured to interact with your locally running Ollama instance. Ensure Ollama is running and the desired model (e.g., `llama2`) is pulled before execution.

### Switching to OpenAI Models

To switch from Ollama local models to OpenAI models for naive RAG, you will typically need to:

1.  **Set your OpenAI API key**:
    Set the `OPENAI_API_KEY` environment variable or directly within your notebook:
    ```python
    import os
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    ```
2.  **Modify LLM initialization**:
    Change the OpenAI LLM initialization code to use OpenAI's client.

## Agent API Usage (AISuite Agent API)

For the agentic RAG implementation, the aisuite Agent API is used. To switch to OpenAI client, refer to [LLM Zoomcamp 2026 - 01-agentic-rag Lessons](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag/lessons). The lessons provide detailed examples and code snippets for implementing agentic RAG with OpenAI models effectively.
