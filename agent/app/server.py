from fastapi import FastAPI
from models.payload import Payload
from models.response import AgentResponse
from agent.main import run_agent_graph

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

    print(payload)

    res = run_agent_graph(user_query=payload.ques, repo_path=payload.repo_path)
    
    return AgentResponse(
        result=res["analysis"],
        numFiles=res["num_files"],
        filesChecked=res["files"]
    )