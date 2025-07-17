"""Text summarization tools."""
from langchain_groq import ChatGroq


def summarize_text(text: str, groq_api_key: str) -> str:
    """Summarize text using Groq.
    
    Args:
        text: The text to summarize
        groq_api_key: API key for Groq
        
    Returns:
        Summarized text
    """
    model = ChatGroq(api_key=groq_api_key, model_name="meta-llama/llama-4-maverick-17b-128e-instruct")
    prompt = f"Summarize this academic paper: {text[:15000]}"
    return model.invoke(prompt).content
