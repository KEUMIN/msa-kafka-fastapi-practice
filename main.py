from fastapi import FastAPI
from routers import inventory_service
import uvicorn

app = FastAPI()

app.include_router(inventory_service.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to our API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)