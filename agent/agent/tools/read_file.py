from langsmith import traceable
from langchain_core.tools import tool

@tool(name_or_callable="read_file", description="Read contents of the file")
@traceable(run_type="tool")
def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # print(content)
            return content
    except FileNotFoundError:
        # print("file not found")
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        # print(f"file not found {e}")
        return f"An error occurred: {e}"
    
# read_file("/Users/kartikgandhi/Documents/codesage/agent/agent/tools/list_files.py")
