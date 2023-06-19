from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Status(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    completed = "completed"


class Task(BaseModel):
    name: str
    description: Optional[str] = Field(None)
    creation_date: datetime
    status: Status
