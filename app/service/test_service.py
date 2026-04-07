
from app.graph.graph import app
from schema import State
from langfuse.langchain import CallbackHandler

async def loop_test(state: State,handler : CallbackHandler):
    ans = await app.ainvoke(state,config={"callbacks": [handler]})
    return ans