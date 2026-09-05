# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create API Routes

#### Description

Use the provided starter code to create a FastAPI application for managing a list of tasks. Add routes that return all tasks and return one task by its ID.

#### Requirements

Completed program should:

- Create a `FastAPI` application.
- Implement `GET /tasks` to return the complete task list as JSON.
- Implement `GET /tasks/{task_id}` to return one task by ID.
- Return a `404` response when the requested task does not exist.

### 🛠️ Add Validated Task Creation

#### Description

Define a Pydantic model for a new task and implement an endpoint that adds tasks to the in-memory list. The endpoint should reject incomplete or invalid request data.

#### Requirements

Completed program should:

- Define a request model with a required non-empty `title` and a `completed` field that defaults to `False`.
- Implement `POST /tasks` to accept a JSON request body and return the created task.
- Assign a unique integer ID to each new task.
- Return an appropriate `201` status code when a task is created.

### 🛠️ Test the API

#### Description

Run the application with Uvicorn and use FastAPI's interactive documentation to test each route.

#### Requirements

Completed program should:

- Start successfully with `uvicorn starter-code:app --reload`.
- Use the `/docs` page to test both successful and unsuccessful requests.
- Demonstrate a successful task lookup, a missing-task `404`, and a validated task creation request.