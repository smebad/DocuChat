import streamlit as st
import PyPDF2
import openai
import os
import pyperclip

# Set page config
st.set_page_config(page_title="DocuChat", page_icon="📄", layout="wide")

# Sidebar configuration
st.sidebar.title("DocuChat")
st.sidebar.info("Interact with PDF documents in your folder.")
openai.api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Contact details
st.sidebar.title("Contact")
st.sidebar.markdown("Created by: [Syed Muhammad Ebad](https://github.com/smebad)")
st.sidebar.markdown("Contact: [Email](mailto:mohammadebad1@hotmail.com)")

# Define function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

# Function to list PDF files in a directory
def list_pdf_files(directory):
    try:
        return [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.lower().endswith('.pdf')]
    except Exception as e:
        st.error(f"Error listing PDF files: {e}")
        return []

# Function to generate questions from text using OpenAI's API
def get_questions_from_gpt(text):
    prompt = text[:4096]  # Adjust as needed to fit within token limit
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=30
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error generating question: {e}")
        return ""

# Function to generate answers to a question using OpenAI's API
def get_answers_from_gpt(text, question):
    prompt = text[:4096] + "\nQuestion: " + question + "\nAnswer:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=2000
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error generating answer: {e}")
        return ""

# Main function of the Streamlit app
def main():
    st.title("DocuChat 📄")
    st.markdown("### Interact with PDF documents in your folder")

    # Get the folder containing PDF files using folder input
    pdf_folder = st.text_input("Enter the folder path containing PDF files:")

    if pdf_folder and os.path.isdir(pdf_folder):
        pdf_files = list_pdf_files(pdf_folder)

        if not pdf_files:
            st.warning("No PDF files found in the specified folder.")
        else:
            st.info(f"Number of PDF files found: {len(pdf_files)}")

            # Select PDF file
            selected_pdf = st.selectbox("Select a PDF file", pdf_files)
            st.info(f"Selected PDF: {selected_pdf}")

            # Extract text from the selected PDF
            text = extract_text_from_pdf(selected_pdf)

            if text:
                # Generate a question from the extracted text using GPT-4
                question = get_questions_from_gpt(text)
                st.write("**Generated Question:** " + question)

                # Create a text input for the user to ask a question
                user_question = st.text_input("Ask a question about the document")

                if user_question:
                    # Generate an answer to the user's question using GPT-4
                    answer = get_answers_from_gpt(text, user_question)
                    st.write("**Answer:** " + answer)
                    if st.button("Copy Answer Text"):
                        pyperclip.copy(answer)
                        st.success("Answer text copied to clipboard!")
    else:
        st.warning("Please enter a valid folder path.")

# Run the main function if the script is being run directly
if __name__ == '__main__':
    main()
