from pydantic import BaseModel
from typing import Any, Literal

class State(BaseModel):
    scope: Literal["local", "remote"]
    label: str

class SimpleState(State):
    type: Literal["str", "int", "float", "bool"]
    default: str | int | float | bool | None

class ChatboxState(State):
    direction: bool
    msg: str

class GPSState(State):
    lat: float
    long: float

class StateStore():
    def __init__(self):
        self.states: dict[str, dict[str, Any]] = {}

    def register(self, state: State):
        self.states[state.label] = state.model_dump()

    def get_ref(self, label: str):
        return self.states[label]

test = []
props = ChatboxState.model_json_schema()['properties']
for p in props:
    test.append((p, props[p]["type"]))
    
print(test)