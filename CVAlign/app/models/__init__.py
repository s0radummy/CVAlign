import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CVUpload(Base):
    __tablename__ = "cv_uploads"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    job_description = Column(String, nullable=False)
    cv_url = Column(String, nullable=False)
    score = Column(String, nullable=False)
