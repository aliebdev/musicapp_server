from fastapi import FastAPI

from database import engine
from models.base import Base
from routes import auth

app = FastAPI()

app.include_router(
    router=auth.router,
    prefix="/auth",
)


Base.metadata.create_all(engine)
