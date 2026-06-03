import asyncio
from fastapi import FastAPI
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
