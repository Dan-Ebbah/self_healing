from typing import Dict, Set, Any

from Planner import bfs_planner
from domain import DataType, Domain, State, Action
from travel_domain import ToolFailure


def run_with_recomposition(
        initial_data: Dict[DataType, Any],
        initial_state: Set[DataType],
        domain: Domain,
        goal: DataType,
):
    state_types: State = set(initial_state)
    state_data: Dict[DataType, Any] = dict(initial_data)
    planner_calls = 0
    tool_calls = 0

    planner = bfs_planner(domain, state_types, goal)
    planner_calls += 1
    if planner is None:
        print("No plan found")
        return None

    idx = 0
    while idx < len(planner):
        action = planner[idx]
        print(f"Run (recompose) - Executing action: {action.name}")

        try:
            if action.impl is None:
                for effect in action.effects:
                    state_data[effect] = f"{effect.name}_value"
            else:
                result = action.impl(state_data)
                state_data.update(result)
                tool_calls += 1

            state_types |= action.effects
            idx += 1

        except ToolFailure as e:
            print(f"Failure in: ({action.name.upper()}): {e}. Replanning...")
            domain = _remove_action(domain, action)
            planner = bfs_planner(domain, state_types, goal)
            planner_calls += 1
            if planner is None:
                print("No plan found after failure")
                break
            idx = 0

    print(f"Planner calls: ({planner_calls})")
    print(f"Tool calls: ({tool_calls})")
    print(f"Goal present?: {goal in state_types}")
    return state_data

def _remove_action(domain: Domain, action: Action) -> Domain:
    new_actions = [a for a in domain.actions if a != action]
    return Domain(name=domain.name, data_types=domain.data_types, actions=new_actions)