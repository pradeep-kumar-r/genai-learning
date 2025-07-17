#!/usr/bin/env python
"""Test script for the research agent."""
from src.utils.config import load_api_keys
from src.agent.runner import run_research_query


def test_research_agent():
    """Test the research agent with a simple query."""
    print("\n===== TESTING RESEARCH AGENT =====\n")
    
    # Load API keys
    try:
        groq_api_key, openai_api_key = load_api_keys()
        print("✅ API keys loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load API keys: {e}")
        return
    
    # Simple test query
    test_query = "What are the recent advances in transformer architecture?"
    print(f"\n📝 Test query: {test_query}\n")
    
    # Run the query
    try:
        result = run_research_query(test_query, openai_api_key, groq_api_key)
        print("\n===== TEST RESULTS =====\n")
        print(result)
        print("\n===== TEST COMPLETE =====\n")
    except Exception as e:
        print(f"❌ Error running research query: {e}")


if __name__ == "__main__":
    test_research_agent()
