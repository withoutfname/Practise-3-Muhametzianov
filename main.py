from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.events import Event
from models.users import User
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@app.on_event("startup")
async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.planner, document_models=[Event, User])  # 'planner' — имя БД в Mongo

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)