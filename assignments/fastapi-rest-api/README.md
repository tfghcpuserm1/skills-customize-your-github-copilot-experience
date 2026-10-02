# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage a collection of books. Practice defining request models, choosing HTTP methods and status codes, and validating API behavior with interactive documentation.

## 📝 Tasks

### 🛠️ Create the Books Collection API

#### Description
Complete the starter application so a client can list all books and add a new book. Store books in the provided in-memory collection; no database is needed.

#### Requirements
Completed program should:

- Start with `uvicorn starter-code:app --reload` after installing FastAPI and Uvicorn with `pip install fastapi uvicorn`
- Return all books from `GET /books`
- Accept a book with a title and author at `POST /books`, assign it a unique integer ID, and return the created book
- Use the FastAPI docs at `/docs` to try both endpoints

### 🛠️ Add Routes for Individual Books

#### Description
Add routes that find, update, and delete a book by its ID. Use the HTTP methods that fit each operation and return a clear not-found response when the requested ID does not exist.

#### Requirements
Completed program should:

- Return one book from `GET /books/{book_id}`
- Update a book's title and author with `PUT /books/{book_id}`
- Delete a book with `DELETE /books/{book_id}`
- Return HTTP `404` for update, delete, or lookup requests that use an unknown ID

### 🛠️ Validate Requests and Responses

#### Description
Use the provided Pydantic models and FastAPI response handling to make the API's behavior consistent for valid and invalid requests.

#### Requirements
Completed program should:

- Require non-empty title and author values for new and updated books
- Return the created or updated book as JSON, including its ID
- Return HTTP `422` when a request body is missing required fields or contains invalid values
- Verify successful and error cases using `/docs`