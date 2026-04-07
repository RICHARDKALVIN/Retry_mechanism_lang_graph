from typing import TypedDict,Any

class State(TypedDict):
    query : str
    loop_count : int
    retry_count : int 
    url :str
    metadata : dict
    answer : str 
    trace : Any