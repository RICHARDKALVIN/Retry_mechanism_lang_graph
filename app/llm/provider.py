
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,
    api_key= os.getenv("GEMINI_API_KEY"),
    max_output_tokens=100
)