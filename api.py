from fastapi import FastAPI
from todo import todo_router
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Привет Эмиль"}

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)