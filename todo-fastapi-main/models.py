from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    complete = Column(Boolean, default=False)
    #owner_id = Column(Integer, ForeignKey("users.id"))
