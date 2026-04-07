from langgraph.graph import END
import httpx
from app.llm.provider import llm
from langchain_core.output_parsers import StrOutputParser
from langfuse import observe



@observe(name="entry")
def entry(state):
    
    return {"loop_count": 0}


@observe(name="incrementer")
def incrementer(state):
    new_count = state["loop_count"] + 1

    return {"loop_count": new_count}


@observe(name="checker")
def checker(state):
    result = (
        "not done"
        if (state["query"] == "inc" and state["loop_count"] < 5)
        or (state["query"] != "inc" and state["retry_count"] < 3)
        else "done"
    )


    return {"answer": result}


@observe(name="retrieve_documents")
async def execute_node(state):
    count = state.get("retry_count", 0)

    

    try:
        if count == 2:
            url = "https://jsonplaceholder.typicode.com/posts/1"
        else:
            url = state["url"]

        print("Executing node with url:", url)

        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

           

            if response.status_code == 200:
                data = response.json()

                

                return {
                    "metadata": data,
                    "retry_count": count + 1
                }
            else:
               

                return {
                    "answer": f"failed {response.status_code}",
                    "retry_count": count + 1
                }

    except Exception as e:
       
        return {
            "answer": "failed with error",
            "retry_count": count + 1
        }


@observe(name="llm_call")
async def llm_node(state):
    prompt = f"what does this data mean? {state['metadata']}"

   

    try:
        response_text = await (llm | StrOutputParser()).ainvoke(prompt)

        

        return {"answer": response_text}

    except Exception as e:
       
        raise