from fastapi import FastAPI

from app.api.sessions import sessions_router

app = FastAPI()
app.include_router(sessions_router)
