# Task API

A simple REST API built with Python and FastAPI as part of my Week 2 internship assignment.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Git and GitHub

## Run Locally

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Start the server

```powershell
python -m uvicorn main:app --reload --port 8000
```

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |

## Interactive Documentation

Once the server is running, visit:

http://localhost:8000/docs

## Project Status

- [x] Stage 0: Hello server
- [ ] Stage 1: Root and health endpoints
- [ ] Stage 2: Read tasks
- [ ] Stage 3: Create tasks
- [ ] Stage 4: Update and delete tasks
- [ ] Stage 5: Swagger UI verification
- [ ] Stage 6: GitHub publication
