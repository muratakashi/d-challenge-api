# from typing import Optional

from typing import List

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.requests import Request

from database import SessionLocal
from tripcost import models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/tripcost")
def tripcost_findall(db: Session = Depends(get_db)):
    tripcost = schemas.TripCost.select()
    return tripcost


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


