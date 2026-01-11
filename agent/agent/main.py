from typing import Literal
from langsmith import traceable
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain.messages import SystemMessage, HumanMessage

from constants import SYSTEM_PROMPT
from agent.tools.read_file import read_file
from agent.tools.list_files import list_files
from agent.clients.ollama import ollama_client
from agent.state.agent_state import AgentState
from agent.tools.final_answer import final_answer

llm = ollama_client

available_tools = [list_files, read_file, final_answer]
tool_mapping = {tool.name: tool for tool in available_tools}

llm_with_tools = llm.bind_tools(available_tools)

@traceable(run_type="llm")
def llm_call(state: AgentState) -> AgentState:
    """Performs the LLM call"""

    messages = state["messages"]
    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        tool_call = response.tool_calls[0]

        # Final structured output
        if tool_call["name"] == "final_answer":
            return {
                **state,
                "final_result": tool_call["args"],
                "messages": messages + [response],
            }

        # Any other tool → let LangGraph route it
        return {
            **state,
            "messages": messages + [response],
        }

    if state.get("final_result"):
        return state

    # raise RuntimeError("LLM did not call a tool when one was expected")
    return state

tool_node = ToolNode([list_files, read_file, final_answer])

@traceable
def end_loop(state: dict):
    return state

@traceable
def should_continue(state: dict) -> Literal["tool_node", "end_loop"]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    if state.get("final_result"):
        return "end_loop"

    messages = state["messages"]
    last_message = messages[-1]

    print("tool calls", last_message.tool_calls)

    if last_message.tool_calls:
        return "tool_node"

    return "end_loop"

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("llm_call", llm_call)
    graph.add_node("tool_node", tool_node)
    graph.add_node("end_loop", end_loop)

    graph.set_entry_point("llm_call")

    graph.add_conditional_edges("llm_call", should_continue)
    graph.add_edge("tool_node", "llm_call")

    compiled_graph = graph.compile()
    return compiled_graph

def run_agent_graph(user_query: str, repo_path: str):
    init_state = AgentState(
        messages=[
            SystemMessage(content=f"{SYSTEM_PROMPT}\nHere is the repository path: {repo_path}"),
            HumanMessage(content=user_query)
        ],
        final_result={}
    )
    
    agent_graph = build_graph()
    
    messages = agent_graph.invoke(init_state, config={"recursion_limit": 50})

    print("final_result:", messages["final_result"])
    print("last message:", messages["messages"][-1].content)
    last_msg = messages["messages"][-1].content
    messages["final_result"]["analysis"] = last_msg if last_msg is not None else messages["final_result"]["analysis"]
    return messages["final_result"] if messages["final_result"] is not None else messages["messages"][-1].content

# run_agent_graph(
#     user_query="is this a monorepo?",
#     repo_path="/Users/kartikgandhi/Documents/codesage/"
# )
