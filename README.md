# 🚀 PDFtoDOCX: Conversor de Documentos de Alta Fidelidade

**Versão em Inglês:** [README-us.md](https://github.com/fhaelmarinho/PDFtoDOCX/blob/main/README-us.md)

| Status do Build | Cobertura de Testes | Licença |
| :---: | :---: | :---: |
| [![Build Status](https://img.shields.io/badge/Build-Passando-brightgreen)](link-para-github-actions) | [![Test Coverage](https://img.shields.io/badge/Coverage-85%25-yellowgreen)](link-para-relatorio-de-testes) | [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) |

## Visão Geral

Este projeto é um conversor desktop de arquivos PDF para DOCX, desenvolvido com **Python** e uma **interface gráfica (GUI)** simples baseada em `tkinter`. Ele transforma a conversão de documentos em um processo rápido e confiável, mantendo a responsividade da aplicação mesmo com arquivos grandes através do uso de processamento assíncrono.



---

## Recursos Chave

O projeto foca em entregar uma experiência robusta e eficiente ao usuário, demonstrando as seguintes habilidades técnicas:

* **Interface Gráfica Intuitiva:** Desenvolvida com `tkinter` para uma experiência desktop nativa e simplificada.
* **Processamento Assíncrono (Threading):** A conversão de arquivos é executada em uma *thread* separada para evitar que a GUI congele (*freezing*), garantindo uma excelente User Experience (UX).
* **Tratamento de Exceções:** Notificações claras de sucesso e erro, com tratamento específico para falhas comuns (PDF corrompido, permissão de arquivo negada).
* **Suporte a Testes Automatizados:** Implementação de **Testes Unitários** para a lógica de conversão, garantindo a integridade e a manutenibilidade do código.
* **Distribuição Simplificada:** Pronto para ser empacotado como um executável *standalone* (usando PyInstaller, por exemplo) para fácil distribuição.

---

## 💡 Desafios Técnicos Resolvidos

Esta seção destaca as decisões de engenharia que elevam o projeto:

| Desafio Técnico | Solução Implementada |
| :--- | :--- |
| **Congelamento da Interface (GUI)** | garantindo que permaneça responsiva. |
| **Garantia de Qualidade** | Implementação de uma suíte de testes unitários para a camada de serviço (`ConverterService`), permitindo refatoração segura e validação automática de novas funcionalidades. |
| **Dependência Externa** | Encapsulamento da biblioteca `pdf2docx` em uma classe de conversão, desacoplando a GUI da lógica de terceiros e facilitando a troca futura de bibliotecas, se necessário. |

---

## 🛠️ Tecnologias

* **Linguagem:** Python 3.x
* **GUI:** `tkinter` (para a interface gráfica)
* **Conversão Core:** `pdf2docx` (biblioteca de alta fidelidade para conversão)
* **Boas Práticas:** `unittest` (para testes automatizados)

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
