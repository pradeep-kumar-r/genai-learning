# Research Agent

For every scientist, academic, grad student, and engineer - literature review is a daunting task. We only wish we could automate getting insights and simplify work of finding papers and summarizing them. With advent of AI that is a distinct possibility. In this demo we attempt to build a Research Assistant  agent for this.

This is a simple example of an AI research assistant agent that uses a combination of an LLM & a vector db in an agentic workflow to answer questions about research papers.

# **Building The Research Agent**

We will build an agent in a step by step manner. We will walk through some critical patterns that help us to build the agent.

Following are the patterns we will explore:
1. The Agumented Model
2. Prompt Chaining
3. Routing
4. Parallelization - **Not Implemented**
5. Orchestrator-workers - **Not Implemented**
6. Evaluator-optimizer - **Not Implemented**
7. The Agent

**Image Credits:** We are borrowing some of the images from the [Building Effective Agents by Anthropic]( https://www.anthropic.com/engineering/building-effective-agents) blog. Copyright for those images is with original publishers, we are reusing with gratitute.


## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Groq API key
- ChromaDB API key

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies (requirements.txt)
4. Create API keys for OpenAI, Groq, and ChromaDB
5. Set environment variables (copy .env.example to .env, place it in the root directory and fill in the values)
6. Download the research paper

