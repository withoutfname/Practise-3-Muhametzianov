
from fastapi import FastAPI
from routes.events import event_router
from routes.users import user_router
from database.connection import settings
import uvicorn

app = FastAPI(title="Event Planner API with Beanie")

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def startup_event():
    await settings.initialize_database()


@app.get("/")
async def home():
    return {"message": "Event Planner API is running! Эмиль, всё готово"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)