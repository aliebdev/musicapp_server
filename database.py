from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DTABASE_URL = "postgresql://postgres:test1234@localhost:5432/musicapp"

engine = create_engine(DTABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
