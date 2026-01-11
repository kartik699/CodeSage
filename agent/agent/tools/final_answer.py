from langsmith import traceable
from langchain_core.tools import tool

@tool(name_or_callable="final_answer", description="Returns the final answer as JSON")
@traceable(run_type="tool")
def final_answer(analysis: str, num_files: int, files: list[str]):
    """
    Return the final structured response.
    """
    return {
        "analysis": analysis,
        "num_files": num_files,
        "files": files,
    }
