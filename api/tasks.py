from celery import Celery
import os
from schema import FileResponseCreateSchema
from crud import create_fileresponse
import img2pdf

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="sqla+postgresql://user:password@database:5432/alpha",)


@app.task
def task_img_to_pdf(filename:str):
    try:
        path = 'pdf_files'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(f"pdf_files/{filename[:-4]}.pdf","wb") as f:
            f.write(img2pdf.convert([f'jpg/{filename}']))
    except Exception as e:
        raise Exception(e)

@app.task
def task_save_file_2_db(filename,task_id):
    print("="*98)
    print(filename)
    file_response = FileResponseCreateSchema(file_name=filename,
                                                     task_id=task_id,
                                                     download_link=f"127.0.0.1/download_link/?filename={filename}&format=pdf",
                                                     type="PDF")
    create_fileresponse(file_response)
