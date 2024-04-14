from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoIn:
    task: str
    due: datetime | None

@dataclass
class Todo(TodoIn):
    id: int