
from langgraph.graph import entrypoint, StateGraph, END
from langchain_core.runnables import RunnableLambda

@entrypoint
def build_graph():
    graph = StateGraph(dict)

    def hello_node(state):
        return {"text": "Hello from LangGraph!"}

    graph.add_node("start", RunnableLambda(hello_node))
    graph.set_entry_point("start")
    graph.set_finish_point(END)

    return graph.compile()

