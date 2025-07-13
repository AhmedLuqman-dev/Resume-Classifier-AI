import streamlit as st
import pickle
import re
import PyPDF2

# Load model and vectorizer
with open('resume_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

label_classes = ['Advocate', 'Arts', 'Automation Testing', 'Blockchain', 'Business Analyst',
                 'Civil Engineer', 'Data Science', 'Database', 'DevOps Engineer', 'DotNet Developer',
                 'Electrical Engineering', 'ETL Developer', 'HR', 'Hadoop', 'Health and fitness',
                 'Java Developer', 'Mechanical Engineer', 'Network Security Engineer',
                 'Operations Manager', 'PMO', 'Python Developer', 'Sales', 'SAP Developer',
                 'Testing', 'Web Designing']

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Dark mode styles
st.set_page_config(page_title="AI Resume Classifier", layout="centered", page_icon="📄")
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🤖 AI Resume Classifier</h1>", unsafe_allow_html=True)
st.markdown("### 📥 Drag & drop your PDF resume below:")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"], label_visibility="collapsed")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📄 Extracted Resume Preview")
    st.code(resume_text[:1000] + '...')

    cleaned = clean_text(resume_text)
    vector = tfidf.transform([cleaned]).toarray()
    prediction = model.predict(vector)[0]
    predicted_category = label_classes[prediction]

    st.success(f"✅ Predicted Resume Category: **{predicted_category}**")
