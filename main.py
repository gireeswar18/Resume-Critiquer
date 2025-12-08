import streamlit as st
import PyPDF2
import os
import io
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI powered critics")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

uploaded_file = st.file_uploader("Upload your resume in PDF or TXT", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're applying for (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    
    return uploaded_file.read().decode("utf-8")
    

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any context")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations"""

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            [
                {"role": "user", "parts": [prompt]}
            ]
        )

        st.markdown("Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurered: {str(e)}")