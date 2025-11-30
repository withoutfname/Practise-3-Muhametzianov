from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field as PydanticField
from typing import List, Optional

class Event(Document):
    id: PydanticObjectId = PydanticField(default_factory=PydanticObjectId)
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events"

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book...",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]