
from langgraph.graph import END, StateGraph
from schema import State
from app.nodes.nodes import entry, execute_node, incrementer,checker,llm_node
from app.nodes.edges import looper
from app.nodes.edges import ending,redirect,retry_logic

builder = StateGraph(State)


builder.add_node("entry",entry)
builder.add_node("incrementer",incrementer)
builder.add_node("checker",checker)
builder.add_node("ending",ending)
builder.add_node("execute_node",execute_node)
builder.add_node("llm_node",llm_node)







builder.add_conditional_edges("entry",redirect,["incrementer","execute_node"])
builder.add_conditional_edges("execute_node",retry_logic,["checker","execute_node"])
builder.add_conditional_edges("incrementer",looper,["checker","incrementer"])
builder.add_conditional_edges("checker",ending,["incrementer","llm_node"])
builder.add_edge("llm_node",END)

builder.set_entry_point("entry")



app = builder.compile()