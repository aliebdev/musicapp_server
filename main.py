from fastapi import FastAPI

from database import engine
from models.base import Base
from routes import auth, song

app = FastAPI()

app.include_router(router=auth.router, prefix="/auth")

app.include_router(router=song.router, prefix="/song")


Base.metadata.create_all(engine)
