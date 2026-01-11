import os
from langchain_core.tools import tool
from typing import List
from constants import EXCLUDED_DIRECTORIES, EXCLUDED_FILES
from langsmith import traceable

@tool(name_or_callable="list_files", description="List all the files in a directory")
@traceable(run_type="tool")
def list_files(dir_path: str) -> List[str]:
    files_list = []

    for root, dirnames, filenames in os.walk(dir_path):
        # Remove excluded directories from the walk
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRECTORIES and not d.startswith('.')]
        
        for file in filenames:
            # Skip excluded file types
            if any(file.endswith(ext) for ext in EXCLUDED_FILES):
                continue
            
            # Skip hidden files
            if file.startswith('.'):
                continue
                
            file_path = os.path.join(root, file)
            files_list.append(file_path)

    # print(files_list)
    # print(len(files_list))
    return files_list

# list_files("/Users/kartikgandhi/Documents/codesage/backend")