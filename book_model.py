from pydantic import BaseModel

class BookModel(BaseModel):
    title: str
    author: str
    publication_date: str
    sales_data: str
