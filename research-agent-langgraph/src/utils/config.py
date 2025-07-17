"""Configuration utilities for the research agent."""
import os
from dotenv import load_dotenv


def load_api_keys() -> tuple:
    """Load API keys from environment variables.
    
    Returns:
        Tuple of (groq_api_key, openai_api_key)
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the API keys
    groq_api_key = os.getenv("GROQ_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Check if the keys were found
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    return groq_api_key, openai_api_key
