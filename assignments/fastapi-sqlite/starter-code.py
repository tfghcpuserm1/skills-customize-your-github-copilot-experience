import sqlite3
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DATABASE_PATH = Path(__file__).with_name("books.db")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


@contextmanager
def database_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with database_connection() as connection:
        # TODO: Create the books table if it does not already exist.
        raise NotImplementedError


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(title="Books API", lifespan=lifespan)


@app.get("/books", response_model=list[Book])
def list_books():
    with database_connection() as connection:
        # TODO: Select every book and return the rows as dictionaries.
        raise NotImplementedError


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_input: BookInput):
    with database_connection() as connection:
        # TODO: Insert the book with SQL parameters and return its row, including its ID.
        raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    with database_connection() as connection:
        # TODO: Select the matching book or raise HTTPException with status 404.
        raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    with database_connection() as connection:
        # TODO: Update the matching row or raise HTTPException with status 404.
        raise NotImplementedError


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    with database_connection() as connection:
        # TODO: Delete the matching row or raise HTTPException with status 404.
        raise NotImplementedError