
from app.graph.graph import app
from schema import State

async def loop_test(state: State):
    ans = await app.ainvoke(state)
    return ans