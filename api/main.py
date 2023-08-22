from fastapi import FastAPI ,UploadFile
from celery.result import AsyncResult
import os
from fastapi.responses import FileResponse
from crud import get_file_with_taskid
from tasks import task_img_to_pdf , task_save_file_2_db
from fastapi.responses import JSONResponse
from database import engine
from models import Base



Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/download_link/" ,include_in_schema=False)
async def download_link(format:str,filename:str):
    return FileResponse(f"pdf_files/{filename[:-4]}.{format}", media_type='application/pdf')

@app.get("/tasks/{task_id}")
def task_status(task_id: str):
    """
    Get task status.
    PENDING (waiting for execution or unknown task id)
    STARTED (task has been started)
    SUCCESS (task executed successfully)
    FAILURE (task execution resulted in exception)
    RETRY (task is being retried)
    REVOKED (task has been revoked)
    """
    task = AsyncResult(task_id)
    state = task.state

    if state == "FAILURE":
        error = str(task.result)
        response = {
            "state": state,
            "error": error,
        }
    else:
        response = {
            "state": state,
            "result":str(task.result)
        }
    return response

@app.post("/jpgtopdf/")
async def uploadcookie(file: UploadFile):
    try:
        directory = f"jpg/"
        os.makedirs(directory, exist_ok=True)
        with open(f"jpg/{file.filename}", "wb") as f:
                f.write(await file.read())
                task = task_img_to_pdf.delay(file.filename)
                task_save_file_2_db(file.filename,task.task_id)
        return JSONResponse(content={"message": "File uploaded successfully",'task_id':task.task_id})
    except Exception as e:
        return JSONResponse(content={"message": "An error occurred", "error": str(e)})
    
@app.get("/file_link/")
def get_file_link(task_id:str):
    file =  get_file_with_taskid(task_id)
    return JSONResponse(content={"Download Link": file.download_link})
    