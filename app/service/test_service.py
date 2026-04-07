
from app.graph.graph import app
from schema import State
from app.trace.trace import handler

async def loop_test(state: State):
    ans = await app.ainvoke(state,config={"callbacks": [handler]})
    return ans