from fastapi import APIRouter, status
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from fastapi.exceptions import HTTPException

book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_all_books() -> List[Book]:
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump
    books.append(new_book)

    return new_book

@book_router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch('/{book_id}')
async def update_book(book_id: int, updated_book: BookUpdateModel) -> dict:
    for i, book in enumerate(books):
        if book['id'] == book_id:
            book['title'] = updated_book.title
            book['publisher'] = updated_book.publisher
            book['page_count'] = updated_book.page_count
            book['language'] = updated_book.language

            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> dict:
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books.pop(i)
            return
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")