from pydantic import BaseModel

class Payload(BaseModel):
    ques: str
    repoPath: str