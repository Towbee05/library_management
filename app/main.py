from fastapi import FastAPI
from app.core.database import create_tables
from contextlib import asynccontextmanager
from app.routes.auth import authRouter

@asynccontextmanager
async def lifespan(app: FastAPI): 
    # Initialize db at start
    create_tables()
    print("DB created")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router=authRouter, tags=["auth"], prefix="/auth")

@app.get('/')
async def root():
    return {
        "greetings" : "Hello, world"
    }

@app.get('/health')
async def health():
    return {
        "status": "healthy"
        }

