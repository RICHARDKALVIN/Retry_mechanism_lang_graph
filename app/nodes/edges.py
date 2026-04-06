 



from langgraph.graph import END


def looper(state):
    if state["loop_count"] < 5:
        return "incrementer"
    else:
        return "checker"
    
def ending(state):
    if state["answer"] == "done":
        return END
    else:
        return "incrementer"
    
def redirect(state):
    if state["query"] == "inc":
        return "incrementer"
    else:
        return "execute_node"

def retry_logic(state):

    if state["retry_count"] < 3:
        return "execute_node"
    else:
        return "checker"