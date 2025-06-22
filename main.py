from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Init model
llm = ChatOpenAI()

# Send a test prompt
response = llm.invoke("What's the capital of Sweden?")
print("Response:", response.content)
