from dataclasses import dataclass
from typing import Set, List, Dict, Callable


@dataclass(frozen=True)
class DataType:
    name: str


@dataclass
class Action:
    name: str
    preconditions: Set[DataType]
    effects: Set[DataType]
    impl: Callable | None = None

@dataclass
class Domain:
    name: str
    data_types: Set[DataType]
    actions: List[Action]

State = Set[DataType]