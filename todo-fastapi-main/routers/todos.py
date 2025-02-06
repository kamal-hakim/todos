from typing import List, Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import crud
from database import SessionLocal
from schemas import TodoRequest, TodoResponse

router = APIRouter(
    prefix="/todos"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoRequest, db: Session = Depends(get_db)):
    todo = crud.create_todo(db, todo)
    return todo

@router.get("", response_model=List[TodoResponse])
def get_todos(db: db_dependency, completed: bool = None):
    todos = crud.read_todos(db, completed)
    return todos

@router.put("/{id}")
def update_todo(db: db_dependency, id: int, todo: TodoRequest ):
    todo = crud.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo( db: db_dependency, id: int):
    res = crud.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="to do not found")

""""   
@router.get("/search", response_model=List[TodoResponse])
def search_todos(db: db_dependency, q: str ):
    todos = crud.search_todos(db, q)
    return todos
"""""