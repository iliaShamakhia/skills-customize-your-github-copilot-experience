"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    """The fields a client must provide when creating a task."""

    title: str = Field(min_length=1)
    completed: bool = False


tasks = [
    {"id": 1, "title": "Learn FastAPI routes", "completed": False},
    {"id": 2, "title": "Try the interactive docs", "completed": False},
]


@app.get("/tasks")
def list_tasks():
    """Return all tasks."""
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Return one task or a 404 response."""
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create and return a new task."""
    pass