# Resume-Classifier-AI
A web app that uses NLP and machine learning to classify resumes (PDF) into job categories like Data Science, HR, or Java Developer. Built using TF-IDF and logistic regression on a real-world dataset with drag-and-drop upload and dark mode UI.
---
###🧠 Resume Classifier AI | NLP + Machine Learning + Streamlit

An AI-powered application for automated resume classification using **Natural Language Processing (NLP)** and **Machine Learning**. This tool classifies resumes into job categories like *Data Science*, *Web Developer*, *HR*, and more using a trained model and a streamlined user interface built with **Streamlit**.

---

### 🚀 Key Features

- 📄 **Upload PDF Resumes** via drag-and-drop
- 🧠 **TF-IDF Vectorization** for text processing
- 🤖 **Logistic Regression Classifier** trained on real resume dataset
- 🌙 **Dark Mode UI** + Mobile responsive
- 📊 Predicts across 20+ real-world job roles
- ☁️ Deployed easily on **Streamlit Cloud**

---
### 🗂️ Project Structure
<pre><code>Resume-Classifier-AI/ 
 ├── Resume_classifier_AI.ipynb # Jupyter Notebook used to train and save the model 
 ├── app.py # Streamlit web app to run the classifier 
 ├── resume_model.pkl # Saved trained ML model (Logistic Regression) 
 ├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer 
 └── requirements.txt # Python dependencies for the project</code></pre>
---

### 🔧 Technologies Used

- **Python 3**
- **Scikit-learn**
- **NLTK**
- **PyPDF2**
- **Pandas, NumPy**
- **Streamlit**

---

### 📌 How It Works

1. Upload a resume (PDF)
2. The app extracts text from the file
3. Text is preprocessed and vectorized using `TfidfVectorizer`
4. A trained `LogisticRegression` model predicts the job category
5. The predicted label is displayed to the user in a clean interface

---

### 🌐 Live Demo

🎉 Try the project live, no installation needed:

🔗 [Resume Classifier AI Web App](https://resume-classifier-ai-byahmedluqman.streamlit.app/)

Simply drag and drop your resume (PDF), and the app will predict the job category in seconds.

> ⚠️ For best results, upload English resumes with clear role-related content (no scanned images or graphics-heavy PDFs).

---

### 🛠️ How to Run This Project Locally

##### 1. Clone this repository

- git clone https://github.com/AhmedLuqman-dev/Resume-Classifier-AI.git
- cd Resume-Classifier-AI

- pip install -r requirements.txt

- streamlit run app.py
---
### Example Use Case

 A recruiter uploads 100+ resumes, and this tool can auto-sort them into job categories (e.g., Data Science, HR) for faster filtering and shortlisting.
---
### 📃 License
This project is intended for educational purposes only and is open-source under the MIT License.


