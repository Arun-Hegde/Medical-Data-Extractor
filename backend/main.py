from fastapi import FastAPI,File,UploadFile,Form
import uvicorn
from backend.src.extractor import extract
import uuid
import os

app = FastAPI()


@app.post('/extract_from_doc')
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...)
):
    contents = file.file.read()

    upload_dir = "../uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, str(uuid.uuid4()) + ".pdf")

    with open(file_path, 'wb') as f:
        f.write(contents)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        import traceback
        traceback.print_exc()
        data = {
            'error': str(e)
        }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == '__main__':
    uvicorn.run (app,host='127.0.0.1',port=8000)