from dataclasses import dataclass
from typing import Set, List, Dict, Callable, Optional, Any


@dataclass(frozen=True)
class DataType:
    name: str


@dataclass
class Action:
    name: str
    preconditions: Set[DataType]
    effects: Set[DataType]
    impl: Optional[Callable[[Dict[DataType, Any]], Dict[DataType, Any]]] = None

@dataclass
class Domain:
    name: str
    data_types: Set[DataType]
    actions: List[Action]

State = Set[DataType]