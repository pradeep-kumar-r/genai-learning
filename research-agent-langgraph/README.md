# AI Research Assistant

For every scientist, academic, grad student, and engineer - literature review is a daunting task. We only wish we could automate getting insights and simplify work of finding papers and summarizing them. With advent of AI that is a distinct possibility. In this demo we attempt to build a Research Assistant for this.

This is a modular implementation of an __AI Research Assistant__ using LangGraph and LangChain. The purpose of the research assistant is to take user queries & answer questions about research papers from ArXiv.

This implementation focuses on the Autonomous Agent pattern, where the agent is completely autonomous and non-deterministic. It decides based on an LLM call which actions to take (which tools to call, etc.). It also does observation and evaluation of the results of the actions, reasons about them, and decides on next steps including stopping the computation.

Link to the original GitHub repo -> [https://github.com/Thejaswi05/research_agent_demo](https://github.com/Thejaswi05/research_agent_demo)

# **Modular Structure of the AI Research Assistant**

The research agent has been refactored into a modular structure for better maintainability, testability, and extensibility. Here's an overview of the modular architecture:

## Project Structure

```
research-agent-langgraph/
├── main.py                  # Main entry point
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── src/                   # Source code
│   ├── __init__.py        # Package initialization
│   ├── agent/             # Agent implementation
│   │   ├── __init__.py
│   │   ├── research_agent.py  # Agent definition
│   │   └── runner.py      # Agent execution
│   ├── models/            # Data models
│   │   ├── __init__.py
│   │   └── schemas.py     # Input schemas for tools
│   ├── tools/             # Tool implementations
│   │   ├── __init__.py
│   │   ├── arxiv_tools.py # ArXiv search and download
│   │   ├── summarization.py # Text summarization
│   │   └── tool_factory.py # Tool creation
│   └── utils/             # Utilities
│       ├── __init__.py
│       └── config.py      # Configuration handling
```

## Key Components

1. **Agent Implementation (`src/agent/`)**
   - `research_agent.py`: Defines the research agent and its decision-making process
   - `runner.py`: Provides functions to run research queries

2. **Data Models (`src/models/`)**
   - `schemas.py`: Defines Pydantic models for structured tool inputs

3. **Tools (`src/tools/`)**
   - `arxiv_tools.py`: Functions for searching and downloading papers from ArXiv
   - `summarization.py`: Text summarization using Groq
   - `tool_factory.py`: Factory functions to create tools for the agent

4. **Utilities (`src/utils/`)**
   - `config.py`: Configuration and environment variable handling

## How the Agent Works

The research agent operates as an autonomous agent that can:

1. **Search for papers** on ArXiv based on user queries
2. **Download papers** to extract their content
3. **Summarize text** using Groq's LLM capabilities
4. **Make decisions** about which tools to use and when to finish
5. **Log its decision process** for educational purposes

The agent uses a combination of OpenAI's models for decision-making and Groq's models for summarization, creating a powerful research assistant that can help with literature reviews.

## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Groq API key

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies from [requirements.txt](requirements.txt)
4. Create API keys for OpenAI and Groq
5. Set environment variables:
   ```
   # Create a .env file in the root directory with:
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

You can use the research agent in two ways:

### 1. Command Line Interface

Run the agent from the command line with a research query:

```bash
python main.py --query "What are the latest advancements in quantum error correction?"
```

If you don't provide a query, it will use a default query about fine-tuning in LLMs.

### 2. Import in Your Code

```python
from src.utils.config import load_api_keys
from src.agent.runner import run_research_query

# Load API keys
groq_api_key, openai_api_key = load_api_keys()

# Run a research query
result = run_research_query(
    "What are the latest advancements in quantum computing?", 
    openai_api_key, 
    groq_api_key
)

print(result)
```

## Extending the Agent

The modular structure makes it easy to extend the agent with new capabilities:

1. **Add new tools**: Create new tool functions in the `src/tools/` directory and register them in `tool_factory.py`
2. **Modify agent behavior**: Update the agent implementation in `src/agent/research_agent.py`
3. **Add new models**: Define new schemas in `src/models/schemas.py`

## License

This project is based on the original work by Thejaswi05 and follows the same licensing terms.

---

[Back to main README](../README.md)
