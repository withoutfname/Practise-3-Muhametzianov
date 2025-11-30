from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field as PydanticField
from typing import Optional, List
from models.events import Event

class User(Document):
    id: PydanticObjectId = PydanticField(default_factory=PydanticObjectId)
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class NewUser(User):
    pass