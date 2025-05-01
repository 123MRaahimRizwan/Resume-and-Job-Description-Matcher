# 🧠 Resume Parser & Job Description Matcher  
A smart, AI-powered web app that evaluates how well a resume fits a job description — with semantic matching, Gemini feedback, and skill gap analysis.

![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square&logo=python)  
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask)  
![LLM](https://img.shields.io/badge/LLM-Gemini_Pro-orange?style=flat-square&logo=google)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## ✨ Features

- 🔍 **Semantic Match Score** using `MiniLM` sentence embeddings  
- 💬 **AI Feedback** via Gemini Pro (Gemini 2.0 API integration)  
- 📊 **Visual Skill Analysis** with pie & bar charts (Matched vs Missing skills)  
- 📄 **PDF Resume Parsing** using `PyPDF2`  
- 📥 **Modern Flask UI** with Bootstrap and loading spinner  
- 🧠 Designed with Transfer Learning + LLM pipeline in mind

---

## 🎯 Use Case

- For students & job seekers to check if their resume fits a job  
- Helps identify missing skills and get AI-powered improvement tips  
- Great tool for **resume tailoring before job/internship applications**

---

## 🖥️ Demo

> 🔗 Live link coming soon!  
> Or run locally using the instructions below.

---

## 🚀 Tech Stack

| Layer        | Tools Used                               |
|--------------|-------------------------------------------|
| Backend      | Flask, Gunicorn                          |
| LLM          | Gemini Pro (`models/gemini-2.0-flash`)    |
| Embeddings   | `sentence-transformers/all-MiniLM-L6-v2` |
| File Parsing | PyPDF2                                   |
| Visuals      | Matplotlib                               |
| UI           | Bootstrap 5 + HTML + CSS + JS Spinner    |

---

## 📦 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/123MRaahimRizwan/Resume-and-Job-Description-Matcher.git
cd resume-matcher
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your Gemini API key**
```bash
# In gen_ai.py
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

4. **Run the Flask app**
```bash
python app.py
```

## 📂 Folder Structure

```bash
resume-matcher/
├── app.py                  # Flask app
├── parser.py               # Resume parsing
├── matcher.py              # Embedding + skill match
├── gen_ai.py               # Gemini Pro feedback
├── visuals.py              # Matplotlib chart generation
├── vector_databases.py     # Skill list
├── static/                 # CSS & images
├── templates/              # HTML files
├── requirements.txt
└── README.md
```

## 🧠 Author

Muhammad Raahim Rizwan
Undergraduate @ NED University of Engineering and Technology
Specializing in Data Science & Computer Vision.

Connect with me on [Linkedin](https://linkedin.com/in/m-raahim-rizwan) and [Github](https://github.com/123MRaahimRizwan)

## 📃 License

MIT — use freely with credit.
