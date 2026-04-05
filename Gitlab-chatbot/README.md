# 🦊 GitLab Handbook AI Assistant

An end-to-end RAG (Retrieval-Augmented Generation) pipeline that allows users to chat with the GitLab Company Handbook using AI. This tool helps employees and candidates instantly find culture and policy information without manual searching.

---

## 🚀 Key Features

* **Semantic Search:** Finds meaning-based matches from the handbook using vector embeddings.
* **Resilient Backend:** Built-in retry logic and error handling for API rate limits.
* **Interactive Chat UI:** Clean, Streamlit-based interface with quick-prompt buttons.
* **Real-time Processing:** Connects to a live FastAPI server for instantaneous retrieval and generation.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **AI Models:** Gemini 1.5 Flash (LLM), Sentence-Transformers `all-MiniLM-L6-v2` (Embeddings)
* **Database:** Supabase (PostgreSQL with `pgvector`)
* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit
* **Data Pipeline:** `requests`, `beautifulsoup4`

---

## 🧠 System Architecture

1. **Ingestion:** `scraper.py` extracts text from GitLab's handbook.
2. **Processing:** `embedder.py` chunks text and generates 384-dimensional vectors.
3. **Storage:** Vectors and metadata are stored in Supabase.
4. **Retrieval:** FastAPI backend queries Supabase for the most relevant context via vector similarity search.
5. **Generation:** Gemini generates a tailored, context-aware answer.

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd Gitlab-chatbot
```

---

### 2. Install Dependencies

Ensure you have activated your virtual environment, then run:

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your credentials:

```env
SUPABASE_URL=https://<your-project-id>.supabase.co
SUPABASE_KEY=<your-anon-public-key>
GEMINI_API_KEY=<your-gemini-api-key>
```

---

### 4. Run the Application

You will need two separate terminal windows.

#### Terminal 1: Start the FastAPI Backend

```bash
python -m uvicorn backend.main:app --reload
```

#### Terminal 2: Start the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

🌐 The application will automatically open in your browser at:
👉 http://localhost:8501

---

## 👨‍💻 Developer

**Ashish Kumar**
B.Tech in Information Technology
Netaji Subhas University of Technology (NSUT) '26

---
