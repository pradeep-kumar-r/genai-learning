"""Research agent implementation."""
from typing import List, Dict, Any
from langchain.agents.agent import AgentExecutor, AgentAction, AgentFinish
from langchain.agents import create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from src.tools.tool_factory import create_structured_tools


def create_research_agent(openai_api_key: str, groq_api_key: str) -> AgentExecutor:
    """Create a research agent using LangChain's AgentExecutor.
    
    Args:
        openai_api_key: API key for OpenAI
        groq_api_key: API key for Groq
        
    Returns:
        Agent executor for research tasks
    """
    # Create the tools
    tools = create_structured_tools(groq_api_key)
    
    # Create the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful AI research assistant. You have access to tools 
         for searching academic papers, downloading paper content, and summarizing text.

            Your approach should be:
            1. Understand the research question
            2. Search for relevant papers using appropriate keywords
            3. Download and analyze the most relevant papers
            4. Synthesize information to answer the question

            Think step by step and make decisions about which tools to use when.
            When you've gathered enough information, provide a comprehensive answer."""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create the model
    model = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")
    
    # Create the agent
    agent = create_openai_tools_agent(model, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        max_iterations=10
    )
    
    return agent_executor


class ResearchAgentWithDecisions(AgentExecutor):
    """Extended AgentExecutor that logs decision points for educational purposes."""
    
    def __init__(self, *args, show_logging=False, show_progress=True, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize decision_log as an instance attribute using object.__setattr__
        # This is necessary because AgentExecutor uses __slots__
        object.__setattr__(self, 'decision_log', [])
        # Control whether to show logging output
        object.__setattr__(self, 'show_logging', show_logging)
        # Control whether to show simplified progress steps
        object.__setattr__(self, 'show_progress', show_progress)
    
    def _call(self, inputs: Dict[str, Any], *args, **kwargs) -> Dict[str, Any]:
        """Override _call to log decision points."""
        
        show_logging = object.__getattribute__(self, 'show_logging')
        if show_logging:
            print("🤖 RESEARCH AGENT INITIATED")
            print(f"📋 Query: {inputs.get('input', '')}")

        # Call the parent class method
        result = super()._call(inputs, *args, **kwargs)

        if show_logging:
            print("\n✨ AGENT EXECUTION COMPLETE")
            print("\n----- DECISION LOG -----")
            decision_log = object.__getattribute__(self, 'decision_log')
            for i, decision in enumerate(decision_log):
                print(f"{i+1}. {decision}")
            print("--------------------------")

        return result

    def _take_next_step(self, name_to_tool_map: Dict[str, Any], color_mapping: Dict[str, str],
                       inputs: Dict[str, Any], intermediate_steps: List[tuple], *args, **kwargs) -> Any:
        """Override to log agent decisions."""

        try:
            result = super()._take_next_step(name_to_tool_map, color_mapping, inputs, intermediate_steps, *args, **kwargs)

            # Log the decision
            if isinstance(result, list):
                for r in result:
                    if isinstance(r, tuple) and isinstance(r[0], AgentAction):
                        action = r[0]
                        decision = f"Decided to use tool: {action.tool} with input: {action.tool_input}"
                        decision_log = object.__getattribute__(self, 'decision_log')
                        decision_log.append(decision)
                        show_logging = object.__getattribute__(self, 'show_logging')
                        show_progress = object.__getattribute__(self, 'show_progress')
                        
                        if show_logging:
                            print(f"\n🔄 Agent Decision: {decision}")
                        elif show_progress:
                            # Display simplified progress messages based on the tool being used
                            if action.tool == "search_arxiv":
                                query = action.tool_input.get('query', '') if isinstance(action.tool_input, dict) else action.tool_input
                                print(f"📚 Searching arXiv for: '{query}'...")
                            elif action.tool == "download_paper":
                                paper_id = action.tool_input.get('paper_id', '') if isinstance(action.tool_input, dict) else action.tool_input
                                print(f"📄 Downloading paper: {paper_id}...")
                            elif action.tool == "summarize_text":
                                print("✏️ Summarizing text...")
                            else:
                                print(f"🔍 Using tool: {action.tool}...")

            elif isinstance(result, AgentFinish):
                decision = f"Decided to finish with output: {result.return_values.get('output', '')[:100]}..."
                decision_log = object.__getattribute__(self, 'decision_log')
                decision_log.append(decision)
                show_logging = object.__getattribute__(self, 'show_logging')
                show_progress = object.__getattribute__(self, 'show_progress')
                
                if show_logging:
                    print(f"\n✅ Agent Finish: {decision}")
                elif show_progress:
                    print("✨ Synthesizing final answer...")


            return result

        except (ValueError, KeyError, TypeError) as e:
            # Catch specific exceptions instead of a general Exception
            show_logging = object.__getattribute__(self, 'show_logging')
            if show_logging:
                print(f"Error in agent execution: {e}")
            return AgentFinish(return_values={"output": f"An error occurred during execution: {str(e)}"}, log=f"Error: {str(e)}")
        except Exception as e:
            # Still catch general exceptions as a fallback, but with more detailed error handling
            show_logging = object.__getattribute__(self, 'show_logging')
            if show_logging:
                print(f"Unexpected error in agent execution: {e}")
            return AgentFinish(return_values={"output": "An unexpected error occurred during execution."}, log=f"Unexpected error: {str(e)}")
