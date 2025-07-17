"""Input schemas for the research agent tools."""
from pydantic import BaseModel, Field


class SearchArxivInput(BaseModel):
    """Input schema for searching arXiv."""
    query: str = Field(description="The search query for arXiv papers")
    max_results: int = Field(default=5, description="Maximum number of results")


class DownloadPaperInput(BaseModel):
    """Input schema for downloading a paper."""
    paper_id: str = Field(description="The arXiv paper ID to download")


class SummarizeTextInput(BaseModel):
    """Input schema for text summarization."""
    text: str = Field(description="The text to summarize")
