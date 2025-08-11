import uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 300,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Melé",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 420,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The WebSocket Handbook",
        "author": "Alex Diaconu",
        "publisher": "Practical Guides",
        "published_date": "2021-01-01",
        "page_count": 240,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2015-08-20",
        "page_count": 792,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Clean Code in Python",
        "author": "Mariano Anaya",
        "publisher": "Packt Publishing",
        "published_date": "2018-08-29",
        "page_count": 330,
        "language": "English",
    },
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

@app.get('/books', response_model=List[Book])
async def get_all_books() -> List[Book]:
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump
    books.append(new_book)

    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch('/book/{book_id}')
async def update_book(book_id: int, updated_book: BookUpdateModel) -> dict:
    for i, book in enumerate(books):
        if book['id'] == book_id:
            book['title'] = updated_book.title
            book['publisher'] = updated_book.publisher
            book['page_count'] = updated_book.page_count
            book['language'] = updated_book.language

            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> dict:
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books.pop(i)
            return
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

def main():
    """Starts the Uvicorn server programmatically."""
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
