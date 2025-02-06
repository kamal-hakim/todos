from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    description: str = Field(min_length=3)
    complete: bool = Field(default=False)

class TodoResponse(BaseModel):
    id: int
    description: str
    complete: bool

class Config:
    orm_mode = True