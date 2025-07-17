"""Tools for interacting with arXiv."""
import arxiv
import requests
import PyPDF2
from io import BytesIO
from typing import List, Dict, Any


def search_arxiv(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """Search for papers on arXiv and return basic info.
    
    Args:
        query: The search query for arXiv papers
        max_results: Maximum number of results to return
        
    Returns:
        List of dictionaries containing paper information
    """
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results)

    results = []
    for paper in client.results(search):
        results.append({
            "id": paper.entry_id.split("/")[-1],
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "url": paper.pdf_url
        })
    return results


def download_paper(paper_id: str) -> str:
    """Download a paper from arXiv by ID and extract text.
    
    Args:
        paper_id: The arXiv paper ID to download
        
    Returns:
        Extracted text from the paper (truncated to 5000 chars)
    """
    search = arxiv.Search(id_list=[paper_id])
    client = arxiv.Client()
    paper = next(client.results(search))

    response = requests.get(paper.pdf_url)
    pdf_file = BytesIO(response.content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text[:5000]  # Return first 5000 chars for simplicity
