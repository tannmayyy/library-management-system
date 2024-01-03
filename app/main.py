

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_book", response_model=models.BookResponse)
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_book", response_model=models.BookResponse)
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": "created book"},db_book

@app.get("/books/")
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    try:
        book = db.query(models.Book).filter(models.Book.id == book_id).first()
        if book:
            return book
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

