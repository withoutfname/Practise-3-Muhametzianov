# database/connection.py
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, PydanticObjectId
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any, List, Optional
from models.events import Event
from models.users import User


class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb://localhost:27017/planner"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.planner,  # имя базы данных
            document_models=[Event, User]
        )


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()

    async def get(self, id: PydanticObjectId) -> Any:
        return await self.model.get(id)

    async def get_all(self) -> List[Any]:
        return await self.model.find_all().to_list()

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc = await self.get(id)
        if not doc:
            return None
        values = body.dict(exclude_unset=True)
        if values:
            await doc.set(values)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True


settings = Settings()