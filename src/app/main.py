import asyncio
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: Annotated[int, Path(ge=1, description="Todo ID")],
) -> TodoResponse:
    return TodoResponse(
        id=todo_id,
        title="Sample Todo",
        description="This is a sample todo",
        completed=False,
    )


@app.post("/todos/preview", response_model=TodoResponse)
def preview_todo(todo: TodoCreate) -> TodoResponse:
    return TodoResponse(
        id=1,
        title=todo.title,
        description=todo.description,
        completed=False,
    )


@app.get("/async-demo")
async def async_demo() -> dict[str, str]:
    await asyncio.sleep(2)
    return {"message": "Async demo response"}
