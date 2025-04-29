from sqlalchemy import create_engine
from models.post import Base
from database.connection import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)