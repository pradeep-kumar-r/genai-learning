from src.utils.config import load_api_keys
from src.agent.research_agent import ResearchAgentWithDecisions, create_research_agent
from src.tools.tool_factory import create_structured_tools


def run_query(passed_query):
    if not passed_query:
        return "WARNING: Empty query. Please provide a query"
    
    groq_api_key, openai_api_key = load_api_keys()
    agent_executor = ResearchAgentWithDecisions(
        agent=create_research_agent(openai_api_key, groq_api_key).agent,
        tools=create_structured_tools(groq_api_key),
        verbose=False,
        max_iterations=10,
        show_logging=False,
        show_progress=True
    )

    result = agent_executor.invoke({"input": passed_query})
    return result["output"]

def main():
    print("\n===== RESEARCH AGENT =====\n")
    print("This agent will help you research academic papers using arXiv.")
    print("It can search for papers, download them, and summarize their content.")
    print("\n=========================\n")
    
    while True:
        print("\n--------------------------")
        user_input = str(input("USER:"))
        print("\n--------------------------")
        print("\nAGENT:")
        print(run_query(user_input))
        print("\n--------------------------")
    

if __name__ == "__main__":
    main()