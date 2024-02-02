from fastapi import FastAPI
import pydantic

ids = []


def unique(value: int) -> int:
    for i in ids:
        if i == value:
            raise ValueError('Duplicate task')
    return value


def unique_validator(field: str) -> classmethod:
    decorator = pydantic.validator(field, allow_reuse=True)
    validator = decorator(unique)
    return validator


class Task(pydantic.BaseModel):
    task_id: int
    name: str
    description: str
    complete: bool

    _unique_id: classmethod = unique_validator("task_id")


app = FastAPI()

tasks = []


@app.get("/tasks/")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task_id(task_id: int):
    return [task for task in tasks if task.task_id == task_id][0]


@app.post("/tasks/")
async def post_task(task: Task):
    tasks.append(task)
    ids.append(task.task_id)
    return task


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, new_task: Task):
    for i in range(len(tasks)):
        if tasks[i].task_id == task_id:
            tasks[i] = new_task
    return new_task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = [task for task in tasks if task.task_id == task_id][0]
    tasks.remove(task)
    return task
