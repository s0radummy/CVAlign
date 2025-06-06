from sqlalchemy import create_engine
from models import Base  

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")
