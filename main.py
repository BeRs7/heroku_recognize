from fastapi import FastAPI, UploadFile
from pytesseract import pytesseract
from PIL import Image

app = FastAPI(docs_url='/')

pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
config = r'--oem 3 --psm 6'


@app.post("/rus/")
async def upload_rus(file: UploadFile):
    img = Image.open(file.file)
    data = pytesseract.image_to_string(img, lang='rus', config=config)
    return {
        "data": data
    }


@app.post("/eng/")
async def upload_eng(file: UploadFile):
    img = Image.open(file.file)
    data = pytesseract.image_to_string(img, config=config)
    return {
        "data": data
    }