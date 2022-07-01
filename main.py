from fastapi import FastAPI, UploadFile
from pytesseract import pytesseract
from PIL import Image
app = FastAPI()

pytesseract.tesseract_cmd = '/Tesseract/tesseract.exe'


@app.post("/pytesseract/")
async def upload_pytesseract(file: UploadFile):
    img = Image.open(file.file)
    config = r'--oem 1 --psm 6'
    ru = pytesseract.image_to_string(img, lang='rus', config=config)
    eng = pytesseract.image_to_string(img, config=config)
    return {
        "RU": ru,
        "ENG": eng
    }