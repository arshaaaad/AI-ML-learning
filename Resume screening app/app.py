import streamlit as st
import pickle
import docx
import PyPDF2
import re

# Load models
svc_model = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))

# Clean text
def cleanResume(txt):
    txt = re.sub(r'http\S+', ' ', txt)
    txt = re.sub(r'@\S+', ' ', txt)
    txt = re.sub(r'#\S+', ' ', txt)
    txt = re.sub(r'RT|cc', ' ', txt)
    txt = re.sub(r'[^\w\s]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    return txt

# PDF extractor
def extract_text_from_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# DOCX extractor
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# TXT extractor
def extract_text_from_txt(file):
    return file.read().decode("utf-8")

# Prediction
def predict_category(resume_text):
    cleaned = cleanResume(resume_text)
    vector = tfidf.transform([cleaned])
    prediction = svc_model.predict(vector)
    return le.inverse_transform(prediction)[0]

# UI
st.set_page_config(page_title="Resume Screening App", layout="centered")

st.title("📄 Resume Screening App")
st.write("Upload resume (PDF / DOCX / TXT)")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            text = extract_text_from_docx(uploaded_file)
        else:
            text = extract_text_from_txt(uploaded_file)

        st.success("Text extracted successfully!")

        if st.checkbox("Show Resume Text"):
            st.text_area("Resume", text, height=300)

        category = predict_category(text)

        st.subheader("Predicted Category:")
        st.success(category)

    except Exception as e:
        st.error(f"Error: {e}")