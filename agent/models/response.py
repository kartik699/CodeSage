from pydantic import BaseModel
from typing import List, Optional

class AgentResponse(BaseModel):
    result: str
    numFiles: Optional[int]
    filesChecked: Optional[List[str]]