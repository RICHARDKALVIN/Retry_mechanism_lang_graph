from typing import TypedDict

class State(TypedDict):
    query : str
    loop_count : int
    retry_count : int 
    url :str
    metadata : dict
    answer : str 