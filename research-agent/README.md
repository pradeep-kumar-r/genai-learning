# Research Agent

For every scientist, academic, grad student, and engineer - literature review is a daunting task. We only wish we could automate getting insights and simplify work of finding papers and summarizing them. With advent of AI that is a distinct possibility. In this demo we attempt to build a Research Assistant for this.

This is a simple example of an AI Research Assistant that uses a combination of an LLM & a vector db in an agentic workflow to answer questions about research papers.

This tutorial is based on a session in a 4-week hands-on training summit organized in 2025 by ODSC (Open Data Science Conference) from Atul Kulkarni & Lakshmithejaswi Narasannagari on "From Concept to Creation: Building Advanced AI Applications with LLM’s and AI Agents".

Link to the original GitHub repo -> [https://github.com/Thejaswi05/research_agent_demo](https://github.com/Thejaswi05/research_agent_demo)

# **Building The Research Agent**

We will build an agent in a step by step manner. First, we will walk through some critical but common workflow patterns using LLMs & tools that help us to build the agent. These are some of the workflow patterns we will explore for our Research Assistant:

__1. Vanilla LLM Augmented__

This workflow pattern is the most basic one. It is a simple LLM call that's augmented with a 3 tools to 
    a. search ArXiv for relevant papers to the query
    b. fetch paper contents 
    c. uses another LLM call to summarize the paper contents.

This is also in a way, a rudimentary emulation of a RAG workflow.

__2. Prompt Chaining__

This workflow pattern chains output of one LLM Call / Tool to the other one.
The research assistant is the orchestrator that coordinates the search and synthesis. search_llm and synthesis_llm are the two LLMs in this workflow. The output of search_llm is fed into the input of synthesis_llm. search_llm is used to convert the user's question into a search query using openai. synthesis_llm is used to synthesize the results of the search using groq.

Unlike agentic systems which are autonomous and non-deterministic, this is a deterministic workflow where we have pre-defined the steps the system will take.

__3. Routing__

This workflow pattern uses a router to route the user's query to the appropriate LLM or tool. An LLM itself or typically a smaller LM is used to evaluate and decide (based on pre-defined rules) which route should the query take.

This is somewhere in between a fully deterministic workflow and an autonomous agent.

__4. Fully Autonomous Agent__

This workflow pattern uses an autonomous agent to coordinate the search and synthesis. The agent is completely autonomous and non-deterministic. It decides based on an LLM call itself which actions to take (which LLMs to route to, which tools to call etc.). It also does observation and evaluation of the results of the actions from environment, reason and decide on next steps including stopping the computation.

This is the most flexible workflow pattern to emulate complex human workflows but also the most difficult to get right due to the non-deterministic nature (& also volatile) of the system.


## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Groq API key

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies from [requirements.txt](requirements.txt)
4. Create API keys for OpenAI, Groq, and ChromaDB
5. Set environment variables (copy [`.env.example`](.env.example) to `.env`, place it in the root directory and fill in the values)
6. Open [research_agent_demo.ipynb](research_agent_demo.ipynb) in Jupyter Notebook and play around


##
[Back to main README](../README.md)
