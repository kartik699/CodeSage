from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GOOGLE_API_KEY

gemini_client = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1,
    vertexai=None,
    api_key=GOOGLE_API_KEY
)