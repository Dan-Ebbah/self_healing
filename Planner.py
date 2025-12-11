from typing import List, Set, Optional, Dict, Tuple
from domain import Action, DataType, Domain, State


def bfs_planner(domain: Domain, initial: State, goal: DataType) -> Optional[List[Action]]:
    from collections import deque

    start = frozenset(initial)
    queue = deque([start])

    parent: Dict[frozenset, Tuple[frozenset, Action | None]] = {start: (start, None)}

    while queue:
        current_state = queue.popleft()

        if goal in current_state:
            return _reconstruct_plan(parent, current_state)

        for action in domain.actions:
            if action.preconditions.issubset(current_state):
                new_state = frozenset(current_state.union(action.effects))
                if new_state not in parent:
                    parent[new_state] = (current_state, action)
                    queue.append(new_state)

    return None

def _reconstruct_plan(parent: Dict[frozenset, Tuple[frozenset, Action | None]],
                      goal_state: frozenset) -> List[Action]:
    plan: List[Action] = []
    state = goal_state
    while True:
        prev_state, action = parent[state]
        if action is None:
            break
        plan.append(action)
        state = prev_state
    plan.reverse()
    return plan
