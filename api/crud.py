import models, schema
from database import db_context
    
def create_fileresponse(file_response:schema.FileResponseCreateSchema):
    db_file_response = models.FileResponse(**file_response.dict())
    with db_context() as db:
        db.add(db_file_response)
        db.commit()
        db.refresh(db_file_response)
    return db_file_response

def get_file_with_taskid(task_id:str):
    with db_context() as db:
        return db.query(models.FileResponse).filter(models.FileResponse.task_id == task_id).first()