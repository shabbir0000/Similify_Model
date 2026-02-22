# Similify Backend API 🚀  
**AI-Powered Duplicate News Detection System**

Similify Backend is a FastAPI-based NLP service that detects duplicate or highly similar articles using TF-IDF vectorization and cosine similarity scoring.

---

## 📌 Overview

Similify API allows you to:

- Detect duplicate or near-duplicate articles
- Calculate similarity scores
- Flag content above a configurable threshold
- Integrate easily with web or mobile applications

The system loads a pre-trained TF-IDF vectorizer and similarity matrix to deliver fast, real-time responses.

---

## 🧠 How It Works

1. Text cleaning & preprocessing  
2. TF-IDF vector transformation  
3. Cosine similarity computation  
4. Ranking top similar articles  
5. Duplicate detection based on threshold  

---

## 🏗️ Project Structure

```
similify-backend/
│
├── app.py                 # FastAPI main application
├── utils.py               # Cleaning & similarity logic
├── clean_data.csv         # Preprocessed dataset
├── tfidf_matrix.pkl       # Stored TF-IDF matrix
├── vectorizer.pkl         # Saved TF-IDF vectorizer
├── requirements.txt       # Project dependencies
└── README.md
```

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Uvicorn

---

## ✨ Features

- 🔎 Real-time similarity detection
- 📊 Similarity score percentage output
- 🚨 Configurable duplicate threshold (default: 0.80)
- ⚡ High-speed response using precomputed TF-IDF
- 🌍 RESTful API
- 📁 CSV dataset support

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shabbir0000/Similify_Model.git
cd Similify_Model
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger Docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/check-duplicate`

#### Request Body

```json
{
  "text": "Man killed after entering perimeter of Trump’s Mar-a-Lago resort",
  "top_n": 5
}
```

#### Response

```json
{
  "is_duplicate": true,
  "results": [
    {
      "article_id": 25,
      "title": "Government Budget Talks with IMF",
      "source_name": "News Agency",
      "url": "https://example.com/news",
      "similarity_score": 0.87
    }
  ]
}
```

---

## 🎯 Duplicate Threshold

Default threshold:

```
0.80
```

Recommended tuning:

- 0.75 → Less strict
- 0.80 → Balanced (Recommended)
- 0.85 → Very strict duplicate detection

Modify inside your similarity function:

```python
duplicate_threshold = 0.80
```

---

## 🌍 Run with Ngrok (Public API)

Start server:

```bash
uvicorn app:app --reload
```

Then:

```bash
ngrok http 8000
```

Use generated HTTPS URL in your frontend/mobile app.

---

## 📈 Industry Use Cases

- News Agencies
- Content Publishing Platforms
- Plagiarism Detection Systems
- AI Content Validation
- SEO Quality Control

---

## 🔮 Future Improvements

- Semantic similarity (BERT / Transformers)
- Database integration (PostgreSQL / MongoDB)
- Elasticsearch support
- Authentication & Rate limiting
- Docker containerization

---

## 👨‍💻 Author

Muhammad Shabbir 
AI Engineer | NLP & AI Automation Specialist  

---
