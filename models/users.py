
from beanie import Document, Link
from pydantic import EmailStr, BaseModel
from typing import Optional, List
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = None

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str