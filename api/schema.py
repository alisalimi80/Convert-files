from pydantic import BaseModel

class FileResponseBaseSchema(BaseModel):
    file_name : str
    task_id : str | None
    type : str
    download_link :str | None

class FileResponseCreateSchema(FileResponseBaseSchema):
    pass

class FileResponseSchema(FileResponseBaseSchema):
    id : int 
    class Config:
        orm_mode = True

