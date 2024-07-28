from fastapi import FastAPI
from cache_service.service import CacheService
from dotenv import load_dotenv
import uvicorn
import os

def lifespan(app):
    # before app start
    load_dotenv()

    cache_service = CacheService()
    cache_service.connect()

    yield
    # before app shutdown
    cache_service.disconnect()

app = FastAPI(lifespan=lifespan)


# Start application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port = int(os.getenv("PORT", "8000")), reload=True)