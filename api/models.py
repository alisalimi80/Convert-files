from sqlalchemy import Column, Integer, String
from database import Base


class FileResponse(Base):
    __tablename__ = "file_response"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index = True,  nullable = False)
    task_id = Column(String, nullable = True, index = True)
    type = Column(String, nullable = False)
    download_link = Column(String, nullable = True)
