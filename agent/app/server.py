from fastapi import FastAPI

app = FastAPI(title="CodeSage Agent")

@app.get("/health")
def health():
    return {"status": "agent ok"}