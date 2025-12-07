import os
from pdf2docx import Converter

class ConverterService:
  
    def __init__(self):
      
        pass

    def convert(self, pdf_path: str) -> str:
        """
        Converte um arquivo PDF para DOCX.

        :param pdf_path: Caminho completo para o arquivo PDF.
        :return: Caminho completo para o arquivo DOCX gerado.
        :raises FileNotFoundError: Se o arquivo PDF não existir.
        :raises Exception: Para erros de conversão ou I/O.
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")
        
        # Define o caminho de saída com a extensão .docx
        docx_path = os.path.splitext(pdf_path)[0] + ".docx"
        
        pdf_converter = None
        try:
            pdf_converter = Converter(pdf_path)
            
            pdf_converter.convert(docx_path, start=0, end=None)
            
            return docx_path
        
        except Exception as e:
            # Captura exceções específicas de pdf2docx ou I/O
            raise Exception(f"Falha na conversão do arquivo: {e}")
        
        finally:
            if pdf_converter:
                pdf_converter.close()