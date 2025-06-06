from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class CVMetadata(Base):
    __tablename__ = "cv_metadata"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    file_name = Column(String)
    file_url = Column(String)
    user_id = Column(String, ForeignKey("user.id"))

