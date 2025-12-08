#import tkinter as tk
#from tkinter import messagebox, filedialog
import os
import threading
from converter_service import ConverterService # Importa o serviço criado

class PDFtoDOCXApp(tk.Tk):
    """
    Classe principal da aplicação que gerencia a GUI (tkinter).
    """
    def __init__(self):
        super().__init__()
        self.title("PDF to DOCX Converter")
        self.resizable(width=False, height=False)
        
        # Inicializa o serviço de conversão
        self.converter_service = ConverterService()
        self.file_input = tk.StringVar()
        
        self._setup_ui()

    def _setup_ui(self):
        """Constrói todos os elementos da interface gráfica."""
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        entry = tk.Entry(frame, textvariable=self.file_input, width=60)
        entry.pack()

        # Botão Upload
        botao_adicao = tk.Button(frame, text="Upload", command=self.select_pdf_file)
        botao_adicao.pack(pady=5)
        
        # Botão Converter
        # Adicionando um feedback de status
        self.status_label = tk.Label(frame, text="Pronto para converter.")
        self.status_label.pack(pady=5)

        # O comando chama um método que inicia a thread
        self.conversor = tk.Button(frame, text="Converter", command=self._start_conversion_thread)
        self.conversor.pack(pady=10)

    def select_pdf_file(self):
        """Abre a caixa de diálogo para seleção de arquivos PDF."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], 
                                               title="Selecione um Arquivo PDF")
        if file_path:  
            file_name = os.path.basename(file_path)
            self.file_input.set(file_path) 
            self.status_label.config(text=f"Arquivo selecionado: {file_name}")
            # messagebox.showinfo("Arquivo Selecionado", f"Você selecionou: {file_name}")

    def _start_conversion_thread(self):
        """
        Inicia a conversão em uma thread separada para manter a GUI responsiva.
        """
        pdf_path = self.file_input.get()
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror(title="Erro", message="Selecione um arquivo PDF válido")
            return

        self.conversor.config(state=tk.DISABLED, text="Convertendo...")
        self.status_label.config(text="Conversão em andamento...")
        
        # Cria e inicia a thread
        thread = threading.Thread(target=self._run_conversion, args=(pdf_path,))
        thread.start()

    def _run_conversion(self, pdf_path):
    
        try:
            # Chama o serviço desacoplado
            docx_path = self.converter_service.convert(pdf_path)
            
            # Atualiza a GUI na thread principal após o sucesso
            self.after(0, lambda: self._conversion_finished(True, f"Arquivo convertido com sucesso para: {docx_path}"))
            
        except Exception as e:
            # Atualiza a GUI na thread principal após o erro
            self.after(0, lambda: self._conversion_finished(False, f"Ocorreu um erro durante a conversão: {e}"))
            
    def _conversion_finished(self, success, message):

        self.conversor.config(state=tk.NORMAL, text="Converter")
        self.status_label.config(text="Pronto para converter.")
        
        if success:
            messagebox.showinfo(title="Sucesso", message=message)
        else:
            messagebox.showerror(title="Erro", message=message)

