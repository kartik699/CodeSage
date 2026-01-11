from pydantic import BaseModel, Field
from typing import List, Optional

class AgentOutput(BaseModel):
    analysis: str = Field(..., description="Analysis of the code based on user query")
    num_files: Optional[int] = Field(description="Number of files read")
    files: Optional[List[str]] = Field(description="List of files read")