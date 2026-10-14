# TaskAPI — Task Management REST API

A lightweight REST API built with **Python** and **FastAPI** that implements complete CRUD (Create, Read, Update, Delete) operations for task management. Developed as part of my Week 2 internship assignment to practice backend development, HTTP methods, request validation, API documentation, and Git version control.

Built with in-memory storage, the API provides predictable HTTP status codes, JSON responses, and interactive documentation through Swagger UI.

## Features

- **Create tasks** with automatic ID assignment.
- **Read tasks** individually or retrieve the complete task list.
- **Update tasks** by changing their title, completion status, or both.
- **Delete tasks** by ID.
- **Input validation** for missing or invalid titles and update payloads.
- **HTTP error handling** for invalid requests and unknown task IDs.
- **Health check endpoint** to verify server availability.
- **Interactive API documentation** using automatically generated Swagger UI.
- **In-memory storage** without external database dependencies.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| Swagger UI / OpenAPI | API documentation and interactive testing |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
TaskAPI/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
│   └── swagger-ui.png
└── .venv/                 # Local virtual environment (not committed)
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip
- Git (optional, for cloning the repository)

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/TaskAPI.git
cd TaskAPI
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API server

```bash
python -m uvicorn main:app --reload --port 8000
```

The server will be available at:

- API root: http://localhost:8000/
- Health check: http://localhost:8000/health
- Interactive Swagger UI: http://localhost:8000/docs
- OpenAPI specification: http://localhost:8000/openapi.json

Press `Ctrl + C` to stop the server.

## API Endpoints

The API exposes the following endpoints.

| HTTP Method | Endpoint | Description | Success Status |
|---|---|---|---|
| GET | `/` | Retrieve API information | `200 OK` |
| GET | `/health` | Check server health | `200 OK` |
| GET | `/tasks` | Retrieve all tasks | `200 OK` |
| GET | `/tasks/{task_id}` | Retrieve a task by ID | `200 OK` |
| POST | `/tasks` | Create a new task | `201 Created` |
| PUT | `/tasks/{task_id}` | Update an existing task | `200 OK` |
| DELETE | `/tasks/{task_id}` | Delete a task | `204 No Content` |

## Usage Examples

The examples below use `curl.exe`, which is available on modern Windows installations, as well as `curl` on Linux and macOS.

### 1. Get API information

```bash
curl -i http://localhost:8000/
```

Example response:

```json
{
  "name": "Task API",
  "version": "1.0",
  "endpoints": ["/tasks"]
}
```

### 2. Check server health

```bash
curl -i http://localhost:8000/health
```

Example response:

```json
{
  "status": "ok"
}
```

### 3. Retrieve all tasks

```bash
curl -i http://localhost:8000/tasks
```

Example response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Build a REST API",
    "done": false
  },
  {
    "id": 3,
    "title": "Publish project on GitHub",
    "done": false
  }
]
```

### 4. Retrieve a single task

```bash
curl -i http://localhost:8000/tasks/1
```

Example response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

### 5. Create a task

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk"}'
```

Expected status: `201 Created`.

Example response:

```json
{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

The ID is assigned automatically. The actual ID depends on the current in-memory task list.

### 6. Update a task

Update its title and completion status:

```bash
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Master FastAPI","done":true}'
```

Expected status: `200 OK`.

You can also update only one field:

```bash
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

### 7. Delete a task

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

Expected status: `204 No Content`.

A successful deletion returns an empty response body.

## Error Handling

The API uses HTTP status codes to communicate the result of each request.

| Status Code | Meaning | Example |
|---|---|---|
| `200` | OK | Successful read or update |
| `201` | Created | Task created successfully |
| `204` | No Content | Task deleted successfully |
| `400` | Bad Request | Missing title or invalid update body |
| `404` | Not Found | Requested task ID does not exist |

Example: requesting a nonexistent task.

```bash
curl -i http://localhost:8000/tasks/99
```

Expected response:

```json
{
  "error": "Task 99 not found"
}
```

## Input Validation

The API validates incoming task data before accepting changes.

- A missing or empty title is rejected when creating a task.
- A title containing only whitespace is rejected.
- An update request must contain at least one supported field: `title` or `done`.
- Titles must be non-empty strings.
- The `done` field must be a boolean.
- Requests targeting unknown task IDs return `404 Not Found`.

Invalid request bodies return `400 Bad Request` when handled by the application's validation logic.

## Interactive API Documentation

FastAPI automatically generates OpenAPI documentation from the application and exposes it through Swagger UI.

Open the following URL while the server is running:

**http://localhost:8000/docs**

Use the **Try it out** feature to execute requests directly from the browser. You can create a task, retrieve it, update it, and delete it without using a separate API client.

### Swagger UI Screenshot

![TaskAPI Swagger UI](screenshots/swagger-ui.png)

*Interactive API documentation generated by FastAPI.*

## Storage and Limitations

This project intentionally uses an in-memory Python list instead of a database.

- Tasks exist only while the server process is running.
- Restarting the server restores the three predefined example tasks.
- Data is not persistent between restarts.
- The project is designed as a small learning API rather than a production task management service.

These limitations are intentional for the assignment and provide a foundation for learning database-backed persistence in a future project.

## Learning Outcomes

Through this project, I practiced:

- Designing RESTful API endpoints.
- Understanding HTTP methods and response status codes.
- Working with JSON request and response bodies.
- Implementing CRUD operations.
- Validating client input.
- Handling missing resources with appropriate errors.
- Generating and testing API documentation with Swagger UI.
- Using Git commits to track development progress.
- Preparing a project for publication on GitHub.

## Internship Progress

- [x] Stage 0 — Hello server
- [x] Stage 1 — Root and health endpoints
- [x] Stage 2 — Read endpoints with 404 handling
- [x] Stage 3 — Create endpoint with validation
- [x] Stage 4 — Update and delete endpoints
- [x] Stage 5 — Swagger UI documentation
- [x] Stage 6 — GitHub publication

*Tick each stage only after its requirements have been verified.*

## Future Improvements

Potential extensions include:

- Persistent storage using SQLite or PostgreSQL.
- Automated tests using `pytest` and FastAPI's `TestClient`.
- Task filtering and searching using query parameters.
- Pagination for large task collections.
- More structured request and response schemas.

These improvements are outside the core in-memory CRUD scope of this assignment.

## Author

**Shreyas**

Software Engineering Student | Python | Backend Development

GitHub: [@ifshreyas](https://github.com/ifshreyas)

## License

No license has been specified yet. If you intend to allow others to reuse, modify, or distribute this project, consider adding an appropriate open-source license.
