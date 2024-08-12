from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker
from datetime import datetime
from book_data import book_data
from api_key import validate_api_keys
from book_model import BookModel

app = FastAPI()

# Serve static files
#app.mount("Assignment_2/static", StaticFiles(directory="static"), name="static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database setup
engine = create_engine("sqlite:///books.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(DateTime, nullable=False)
    sales_data = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Populate database with fake data
def populate_db():
    session = Session()
    books = book_data
    for book in books:
        new_book = Book(title=book["title"], author=book["author"], publication_date=book["publication_date"], sales_data=book["sales_data"])
        session.add(new_book)
    session.commit()

# Delete all records from the books table
def clean_db():
    session = Session()
    session.query(Book).delete()
    session.commit()

# The DB is already setup and populated, so we don't need to run these functions every time the app starts
# If you need to clean the data, uncomment the clean_db() function
# clean_db()
# populate_db()


# API endpoints
@app.get("/books/")
def read_books(api_key: str = Depends(validate_api_keys)):
    session = Session()
    books = session.query(Book).all()
    return JSONResponse(content=[{"id": book.id, "title": book.title, "author": book.author, "publication_date": book.publication_date.strftime('%Y-%m-%d'), "sales_data": book.sales_data} for book in books])

@app.get("/books/{book_id}")
def read_book(book_id: int, api_key: str = Depends(validate_api_keys)):
    session = Session()
    # TODO 1: 
    # 1. Query the database to get the book with the given ID
    # 2. Return a JSONResponse with the book data

# ///////////////////////////////////////////////////  
@app.get("/books/{book_id}")
def read_book(book_id: int, api_key: str = Depends(validate_api_keys)):
    session = Session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return JSONResponse(content={
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "publication_date": book.publication_date.strftime('%Y-%m-%d'),
        "sales_data": book.sales_data
    })

#///////////////////////////////////////////////////
@app.post("/books/")
def create_book(book: BookModel, api_key: str = Depends(validate_api_keys)):
    session = Session()
    new_book = Book(
        title=book.title, 
        author=book.author, 
        publication_date=datetime.strptime(book.publication_date, '%Y-%m-%d'), 
        sales_data=book.sales_data
    )
    session.add(new_book)
    session.commit()
    # TODO 2: 
    # 1. Return a JSONResponse with the new book data
    # 2. Include the ID of the new book in the response

#////////////////////////////////////////////////////////
@app.post("/books/")
def create_book(book: BookModel, api_key: str = Depends(validate_api_keys)):
    session = Session()
    new_book = Book(
        title=book.title, 
        author=book.author, 
        publication_date=datetime.strptime(book.publication_date, '%Y-%m-%d'), 
        sales_data=book.sales_data
    )
    session.add(new_book)
    session.commit()
    return JSONResponse(content={
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
        "publication_date": new_book.publication_date.strftime('%Y-%m-%d'),
        "sales_data": new_book.sales_data
    })

#////////////////////////////////////////////////////////

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookModel, api_key: str = Depends(validate_api_keys)):
    session = Session()
    # TODO 3:
    # 1. Query the database to get the book with the given ID
    # 2. Update the book data with the new data
    # 3. Commit the changes
    # 4. Return a JSONResponse with the updated book data
#/////////////////////////////////////////////////////////////////
@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookModel, api_key: str = Depends(validate_api_keys)):
    session = Session()
    book_to_update = session.query(Book).filter(Book.id == book_id).first()
    if not book_to_update:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_to_update.title = book.title
    book_to_update.author = book.author
    book_to_update.publication_date = datetime.strptime(book.publication_date, '%Y-%m-%d')
    book_to_update.sales_data = book.sales_data
    
    session.commit()
    return JSONResponse(content={
        "id": book_to_update.id,
        "title": book_to_update.title,
        "author": book_to_update.author,
        "publication_date": book_to_update.publication_date.strftime('%Y-%m-%d'),
        "sales_data": book_to_update.sales_data
    })

#/////////////////////////////////////////////////////////////////
@app.delete("/books/{book_id}")
def delete_book(book_id: int, api_key: str = Depends(validate_api_keys)):
    session = Session()
    # TODO 4:
    # 1. Query the database to get the book with the given ID
    # 2. Delete the book
    # 3. Commit the changes
    # 4. Return a JSONResponse with a message indicating success

#////////////////////////////////////////////////////////////////////////
@app.delete("/books/{book_id}")
def delete_book(book_id: int, api_key: str = Depends(validate_api_keys)):
    session = Session()
    book_to_delete = session.query(Book).filter(Book.id == book_id).first()
    if not book_to_delete:
        raise HTTPException(status_code=404, detail="Book not found")
    
    session.delete(book_to_delete)
    session.commit()
    return JSONResponse(content={"message": "Book deleted successfully"})

#////////////////////////////////////////////////////////////////////////