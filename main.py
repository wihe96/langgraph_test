from langgraph.graph import StateGraph, END
from langgraph.graph.runner import RunnableGraph
from langgraph.graph.entrypoint import entrypoint
from langchain_core.runnables import RunnableLambda

@entrypoint
def build_graph() -> RunnableGraph:
    builder = StateGraph(dict)

    def hello_world(state):
        return {"message": "Hello from LangGraph!"}

    builder.add_node("start", RunnableLambda(hello_world))
    builder.set_entry_point("start")
    builder.set_finish_point(END)

    return builder.compile()