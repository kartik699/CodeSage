import uvicorn
from app.config import PORT

def run_server():
    uvicorn.run("server:app", port=PORT, host="localhost", reload=True)

if __name__ == "__main__":
    run_server()