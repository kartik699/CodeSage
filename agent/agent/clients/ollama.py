from langchain_ollama import ChatOllama

ollama_client = ChatOllama(
    model="qwen3-coder:480b-cloud",
    temperature=0.8
)