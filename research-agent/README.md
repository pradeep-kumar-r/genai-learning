# Research Agent

For every scientist, academic, grad student, and engineer - literature review is a daunting task. We only wish we could automate getting insights and simplify work of finding papers and summarizing them. With advent of AI that is a distinct possibility. In this demo we attempt to build a Research Assistant  agent for this.

This is a simple example of an AI research assistant agent that uses a combination of an LLM & a vector db in an agentic workflow to answer questions about research papers.

# **Building The Research Agent**

We will build an agent in a step by step manner. We will walk through some critical patterns that help us to build the agent. These are some of the workflow patterns we will explore for our agent:
1. Vanilla LLM Augmented
2. Prompt Chaining
3. Routing 
4. Autonomous Agent

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