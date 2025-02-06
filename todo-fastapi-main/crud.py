from sqlalchemy.orm import Session
from models import Todos
from schemas import TodoRequest

def create_todo(db: Session, todo_request: TodoRequest):
    todo = Todos(**todo_request.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def read_todos(db: Session, complete: bool):
    if complete is None:
        return db.query(Todos).all()
    else:
        return db.query(Todos).filter(Todos.complete == complete).all()

def update_todo(db: Session, id: int, todo: TodoRequest):
    db_todo = db.query(Todos).filter(Todos.id == id).first()
    if db_todo is None:
        return None
    db.query(Todos).filter(Todos.id == id).update({'description': todo.description, 'complete': todo.complete})
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, id: int):
    todo = db.query(Todos).filter(Todos.id == id).first()
    if todo is None:
        return None
    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()
    return True

"""""
def search_todos(db: Session, q: str):
    return db.query(Todos).filter(Todos.description.ilike(f"%{q}%")).all()
"""""