import os
import logging
import shutil
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from converter_service import ConverterService

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Configurações
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
STYLES_FOLDER = 'statics'

# Garante que os diretórios necessários existam
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STYLES_FOLDER, exist_ok=True)


app = FastAPI()
templates = Jinja2Templates(directory="templates")

converter_service = ConverterService()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Monta o diretório 'statics' para servir arquivos CSS
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_file(request: Request, pdf_file: UploadFile = File(...)):
    if not pdf_file or not allowed_file(pdf_file.filename):
        # Em um app real, você poderia redirecionar com uma query string de erro
        # return RedirectResponse(url="/?error=Arquivo inválido", status_code=303)
        return templates.TemplateResponse("index.html", {"request": request, "error": "Arquivo inválido. Apenas PDFs são permitidos."})

    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    try:
        docx_path = converter_service.convert(pdf_path)
        return FileResponse(path=docx_path, filename=os.path.basename(docx_path), media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    except Exception as e:
        logging.error(f"Erro na conversão: {e}")
        return templates.TemplateResponse("index.html", {"request": request, "error": f"Ocorreu um erro: {e}"})
