# 📄 Resume Critiquer – Streamlit App

A simple AI-powered application that analyzes and critiques resumes using Gemini AI. Built with Python and Streamlit.

## 🚀 Features

1. Upload resume (PDF)

2. AI-powered resume critique

3. Improvement suggestions

4. Clean and interactive UI

5. Lightweight & fast

## 🧰 Tech Stack

* Python 3.11

* Streamlit

* Google Gemini API

* PyPDF2

## 📁 Project Structure

├── main.py <br>
├── requirements.txt <br>
├── Dockerfile <br>
└── README.md

## ▶️ Run Locally
### 1️⃣ Create & activate virtual environment (recommended)

#### Windows
``` 
python -m venv venv
venv\Scripts\activate
```

####  Mac/Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API Key

#### Set your API key in terminal:

#### Windows
```
set GOOGLE_API_KEY=your_key_here
```

#### Mac/Linux
```
export GOOGLE_API_KEY="your_key_here"
```

### 4️⃣ Run the Streamlit app
```
streamlit run main.py
```

### App opens at:
👉 http://localhost:8501


## 🐳 Run with Docker
### Build the image
```
docker build -t resume-critiquer .
```

### Run the container
```
docker run -p 8501:8501 -e GOOGLE_API_KEY="your_key_here" resume-critiquer
```

## 📄 License

Open source. Free to use.

## ✨ Author
Gireeswar C P

email: gireeswarcp18@gmail.com

linkedin: [Gireeswar C P](https://www.linkedin.com/in/gireeswarcp18/)