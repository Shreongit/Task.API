
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse, Response

app = FastAPI(
    title="Task API",
    version="1.0",
    description=(
        "A simple in-memory task management API. "
        "Supports creating, reading, updating, and deleting tasks."
    ),
)


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": False},
    {"id": 3, "title": "Publish project on GitHub", "done": False},
]


@app.get("/", description="Get information about the Task API.")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


@app.get("/health", description="Check whether the API is running.")
def health():
    return {"status": "ok"}


@app.get(
    "/tasks",
    description="Retrieve all tasks stored in memory.",
    response_description="List of tasks",
)
def get_tasks():
    return tasks


@app.get(
    "/tasks/{task_id}",
    description="Retrieve a single task by its ID.",
    responses={404: {"description": "Task not found"}},
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {task_id} not found"},
    )


@app.post(
    "/tasks",
    status_code=201,
    description="Create a task with a title. The ID is generated automatically.",
    responses={400: {"description": "Invalid or missing title"}},
)
def create_task(
    payload: dict = Body(
        ...,
        example={"title": "Buy milk"},
        description="The new task's title.",
    ),
):
    title = payload.get("title")

    if not isinstance(title, str) or not title.strip():
        return JSONResponse(
            status_code=400,
            content={
                "error": "Title is required and must be non-empty text"
            },
        )

    next_id = max((task["id"] for task in tasks), default=0) + 1

    new_task = {
        "id": next_id,
        "title": title.strip(),
        "done": False,
    }

    tasks.append(new_task)

    return JSONResponse(status_code=201, content=new_task)


@app.put(
    "/tasks/{task_id}",
    description="Update a task's title, completion status, or both.",
    responses={
        400: {"description": "Invalid update body"},
        404: {"description": "Task not found"},
    },
)
def update_task(
    task_id: int,
    payload: dict = Body(
        ...,
        example={"title": "Buy groceries", "done": True},
    ),
):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"},
        )

    if not payload:
        return JSONResponse(
            status_code=400,
            content={"error": "Request body must not be empty"},
        )

    if "title" in payload:
        title = payload["title"]
        if not isinstance(title, str) or not title.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Title must be non-empty text"},
            )

    if "done" in payload and not isinstance(payload["done"], bool):
        return JSONResponse(
            status_code=400,
            content={"error": "Done must be a boolean"},
        )

    if not any(field in payload for field in ("title", "done")):
        return JSONResponse(
            status_code=400,
            content={"error": "Provide title or done to update"},
        )

    if "title" in payload:
        task["title"] = payload["title"].strip()

    if "done" in payload:
        task["done"] = payload["done"]

    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    description="Delete a task by its ID.",
    responses={404: {"description": "Task not found"}},
)
def delete_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"},
        )

    tasks.remove(task)
    return Response(status_code=204)
