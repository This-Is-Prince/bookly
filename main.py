import uvicorn
from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

@app.get("/greet/{name}")
async def greet_path(name: str, age: int) -> dict:
    return {"message": f"Hello {name}, age {age}"}

@app.get("/greet")
async def greet_query(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}! and age {age}"}


class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "author": book_data.author,
        "title": book_data.title,
    }


@app.get('/get_headers')
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type

    return request_headers

def main():
    """Starts the Uvicorn server programmatically."""
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
