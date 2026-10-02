from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="A Wrinkle in Time", author="Madeleine L'Engle"),
    2: Book(id=2, title="The Hobbit", author="J.R.R. Tolkien"),
}
next_book_id = 3


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_input: BookInput):
    # TODO: Create a book with the next available ID and return it.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException with status 404.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: Replace the book's title and author, or return a 404 response.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # TODO: Remove the book, or return a 404 response.
    raise NotImplementedError