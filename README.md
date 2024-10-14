# DocuChat 📄 - AI-Powered PDF Interaction App

Welcome to **DocuChat**, an AI-powered app that allows seamless interaction with PDF documents using OpenAI's GPT model. Ask questions about your PDF's content, generate intelligent responses, and copy answers—all through a simple interface! 🧠📑

---

## 🚀 Features

- **Extract Text from PDFs**: Automatically extracts text from your selected PDF files.
- **AI-Powered Q&A**: Uses OpenAI’s GPT-3.5 to generate intelligent questions and answers based on the extracted text.
- **Clipboard Integration**: Easily copy answers to your clipboard with one click.
- **User-Friendly Interface**: Built with Streamlit, offering a clean and intuitive UI.
- **Secure API Key Input**: Input your OpenAI API key securely via the sidebar.

---

## 🛠️ Installation

To set up DocuChat on your local machine, follow these steps:

1. **Clone the repository**:

   ``` bash
   git clone https://github.com/yourusername/DocuChat.git
   cd DocuChat ```

2. **Install dependencies**:

Install the required packages using pip:
  ``` pip install -r requirements.txt ```
  
The requirements.txt file includes the following dependencies:
- openai==1.30.3
- PyPDF2==3.0.1
- pyperclip==1.8.2
- streamlit==1.35.0

3. Run the app:

Launch the Streamlit app:
``` streamlit run app.py ```

🧑‍💻 Usage:

1. Start the app: Once the app is running, it will open in your default web browser.
2. Enter your OpenAI API Key: Input your API key in the sidebar for the app to interact with the OpenAI API.
3. Select a PDF Folder: Enter the folder path where your PDF files are located.
4. Choose a PDF File: Select a PDF file from the dropdown list.
5. Interact with the PDF: The app will extract text from the PDF and generate a sample question. You can also ask your own question and get an AI-powered response.
6. Copy Answers: Click the "Copy Answer Text" button to copy the AI-generated answer to your clipboard.
