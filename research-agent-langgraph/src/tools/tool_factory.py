"""Factory for creating tools for the research agent."""
from typing import List
from langchain_core.tools import Tool, StructuredTool

from src.tools.arxiv_tools import search_arxiv, download_paper
from src.tools.summarization import summarize_text
from src.models.schemas import SearchArxivInput, DownloadPaperInput, SummarizeTextInput


def create_tools(groq_api_key: str) -> List[Tool]:
    """Create the tools for our agent.
    
    Args:
        groq_api_key: API key for Groq
        
    Returns:
        List of tools for the agent
    """
    tools = [
        Tool(
            name="search_arxiv",
            description="Search for academic papers on arXiv. Input is a search query.",
            func=lambda q: search_arxiv(q)
        ),
        Tool(
            name="download_paper",
            description="Download a paper from arXiv and extract its text. Input is a paper ID.",
            func=lambda id: download_paper(id)
        ),
        Tool(
            name="summarize_text",
            description="Summarize a piece of text. Input is the text to summarize.",
            func=lambda t: summarize_text(t, groq_api_key)
        )
    ]

    return tools


def create_structured_tools(groq_api_key: str) -> List[StructuredTool]:
    """Create structured tools for the agent.
    
    Args:
        groq_api_key: API key for Groq
        
    Returns:
        List of structured tools for the agent
    """
    # Define wrapper functions to properly handle the arguments
    def search_arxiv_wrapper(query: str, max_results: int = 5):
        return search_arxiv(query, max_results)
    
    def download_paper_wrapper(paper_id: str):
        return download_paper(paper_id)
    
    def summarize_text_wrapper(text: str):
        return summarize_text(text, groq_api_key)
    
    tools = [
        StructuredTool.from_function(
            func=search_arxiv_wrapper,
            name="search_arxiv",
            description="Search for academic papers on arXiv",
            args_schema=SearchArxivInput,
        ),
        StructuredTool.from_function(
            func=download_paper_wrapper,
            name="download_paper",
            description="Download a paper from arXiv and extract its text",
            args_schema=DownloadPaperInput,
        ),
        StructuredTool.from_function(
            func=summarize_text_wrapper,
            name="summarize_text",
            description="Summarize a piece of text",
            args_schema=SummarizeTextInput,
        )
    ]

    return tools
