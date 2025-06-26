from langgraph.graph import entrypoint
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

@entrypoint
def build_graph():
    graph = StateGraph(dict)

    def hello(state):
        return {"msg": "Hello from LangGraph!"}

    graph.add_node("start", RunnableLambda(hello))
    graph.set_entry_point("start")
    graph.set_finish_point(END)

    return graph.compile()
