import os
from io import BytesIO

import streamlit as st
import openai
import pandas as pd
from docx import Document
import pdfplumber
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Read API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Financial Statement Casting")

uploaded_file = st.file_uploader(
    "Upload a financial statement",
    type=["pdf", "docx", "xlsx", "xls"],
)

file_text = ""

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        # Handle PDF files
        with pdfplumber.open(BytesIO(uploaded_file.read())) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            file_text = "\n".join(pages)
    elif uploaded_file.name.endswith(".docx"):
        # Handle Word documents
        document = Document(uploaded_file)
        file_text = "\n".join([p.text for p in document.paragraphs])
    else:
        # Handle Excel files
        df = pd.read_excel(uploaded_file)
        file_text = df.to_csv(index=False)

if file_text:
    if st.button("Analyze"):
        with st.spinner("Processing with OpenAI..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "Provide a concise analysis of the following financial statement:\n" + file_text
                        ),
                    }
                ],
                max_tokens=200,
            )
        st.subheader("Result")
        st.write(response.choices[0].message.content)
