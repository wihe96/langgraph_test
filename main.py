from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

def build_graph():
    graph = StateGraph(dict)

    def hello_node(state):
        return {"text": "Hello from LangGraph!"}

    graph.add_node("start", RunnableLambda(hello_node))
    graph.set_entry_point("start")
    graph.set_finish_point("start")  # <-- FIXED

    return graph.compile()  