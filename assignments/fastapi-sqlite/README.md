# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Update the books API to store its records in a SQLite database instead of an in-memory collection. Keep the existing REST routes working and make sure book data is still available after the server restarts.

## 📝 Tasks

### 🛠️ Create the Books Database

#### Description
Complete the database initialization function in the starter app. Use Python's built-in `sqlite3` module to create the books table when the FastAPI application starts.

#### Requirements
Completed program should:

- Create a `books` table with an integer primary-key ID, a title, and an author
- Create the table if it does not already exist
- Store the database in a `books.db` file beside the starter application

### 🛠️ Connect the REST Routes to SQLite

#### Description
Replace the in-memory storage behavior by implementing each route with SQLite queries. Use SQL parameters instead of inserting user-provided values directly into query strings.

#### Requirements
Completed program should:

- Make `GET /books` and `GET /books/{book_id}` read book records from SQLite
- Make `POST /books`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}` change records in SQLite
- Preserve the existing JSON response shapes and return HTTP `404` when a requested book does not exist
- Use parameterized SQL for all values supplied by a request

### 🛠️ Verify Persistent Data

#### Description
Run the API, create and update books, then stop and restart the server to check that the database preserves the changes.

#### Requirements
Completed program should:

- Start with `uvicorn starter-code:app --reload` after installing FastAPI and Uvicorn with `pip install fastapi uvicorn`
- Show newly created and updated books after restarting the server
- Continue to support the routes through FastAPI's interactive docs at `/docs`