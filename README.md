# PDF to DOCX Converter

## Objetivo
Este projeto tem como objetivo fornecer uma interface gráfica simples para converter arquivos PDF em arquivos DOCX utilizando a biblioteca `pdf2docx`.

## Funcionalidades
- Seleção de arquivos PDF através de uma interface gráfica.
- Conversão de arquivos PDF para DOCX.
- Notificações de sucesso e erro durante o processo de conversão.

## Requisitos
- Python 3.x
- Bibliotecas: `tkinter`, `pdf2docx`

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/fhaelmarinho/PDFtoDOCX.git
    cd PDFtoDOCX
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. Execute o script principal:
    ```bash
    python main.py
    ```

2. Na interface gráfica, clique em "Upload" para selecionar um arquivo PDF.

3. Clique em "Converter" para iniciar a conversão do arquivo PDF para DOCX.

4. Uma mensagem de sucesso ou erro será exibida após a tentativa de conversão.

## Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
