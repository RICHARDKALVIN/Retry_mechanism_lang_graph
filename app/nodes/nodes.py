from langgraph.graph import END
import httpx
from app.llm.provider import llm
from langchain_core.output_parsers import StrOutputParser

def entry(state):
    return {"loop_count": 0}

def incrementer(state):

    return {"loop_count": state["loop_count"] + 1}

def checker(state):


    if (state["query"] == "inc" and state["loop_count"] < 5 ) or (state["query"] != "inc" and state["retry_count"] < 3):
        return {"answer": "not done"}
    else:
        return {"answer": "done"}
    
async def execute_node(state):

    count = state.get("retry_count", 0)
    
    try:
        if count == 2:
            url = "https://jsonplaceholder.typicode.com/posts/1"
        else:
            url = state["url"] 
        print("Executing node with url:", state["url"])
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                
                return {"metadata": response.json(),"retry_count": count+1}
            else :
                
                return {"answer" : f"failed {response.status_code}","retry_count": count+1}
 
    except Exception as e:
        state["retry_count"] += 1
        return {"answer" : f"failed with error","retry_count": count+1}



async def llm_node(state):

    prompt =f"what is the this data mean? {state['metadata']}"
    response_text = await (llm | StrOutputParser()).ainvoke(prompt)
    return {"answer": response_text}


