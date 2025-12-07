import logging
from app import PDFtoDOCXApp

# Configurar logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    try:
        app = PDFtoDOCXApp()
        app.mainloop()
    except Exception as e:
        logging.error(f"Erro ao iniciar aplicação: {e}")