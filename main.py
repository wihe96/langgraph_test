from langgraph.graph import entrypoint
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

@entrypoint
def ask_sweden_capital(state: dict) -> dict:
    response = llm.invoke("What's the capital of Sweden?")
    return {"answer": response.content}