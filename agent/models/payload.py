from pydantic import BaseModel

class Payload(BaseModel):
    ques: str
    repo_path: str