import uuid
from datetime import datetime

from typing import Optional, Dict

from fastapi import FastAPI, HTTPException

from models import Task, Status

app = FastAPI()

tasks: Dict[str, Task] = {}


@app.get("/tasks")
def read_tasks():
    return tasks


@app.post("/tasks")
def create_task(name: str, description: Optional[str] = None):
    task_id = str(uuid.uuid4())
    tasks[task_id] = Task(
        name=name,
        description=description,
        creation_date=datetime.now(),
        status=Status.todo,
    )
    return {"task_id": task_id}


@app.get("/tasks/{task_id}")
def read_task(task_id: str):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}")
def update_task(
    task_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    status: Optional[Status] = None,
):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if name is not None:
        task.name = name

    if description is not None:
        task.description = description

    if status is not None:
        task.status = status

    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}
