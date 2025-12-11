from domain import Action, DataType
from typing import List, Any, Dict

def execute_plan(plan: List[Action], initial_data: Dict[DataType, Any]) -> Dict[DataType, Any]:
    state_data = dict(initial_data)

    for action in plan:
        print(f"Executing action: {action.name}")
        if action.impl is None:
            _execute_logical_action(action, state_data)
        else:
            _execute_tool_action(action, state_data)
    return state_data

def _execute_logical_action(action: Action, state_data: Dict[DataType, Any]):
    for effect in action.effects:
        state_data[effect] = f"{effect.name}_value"

def _execute_tool_action(action: Action, state_data: Dict[DataType, Any]):
    result = action.impl(state_data)
    state_data.update(result)