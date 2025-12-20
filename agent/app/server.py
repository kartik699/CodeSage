import sys
from pathlib import Path

# Add the agent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI
from models.payload import Payload
from models.response import AgentResponse

app = FastAPI(title="CodeSage Agent")

@app.get("/health")
def health():
    return {"status": "agent ok"}

@app.post("/chat")
def run_agent(payload: Payload) -> AgentResponse:
    """
    This function runs the agent which uses tools to analyse the codebase and returns the response to user query
    
    :param payload: Receives user query and repo path
    :type payload: Payload
    :return: Returns the response
    :rtype: str
    """

    return AgentResponse(result=payload.ques, numFiles=2, filesChecked=["package.json", "package-lock.json"])