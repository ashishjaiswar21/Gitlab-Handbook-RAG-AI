# 🦊 GitLab Handbook AI Assistant

---

## 🔗 Official  Links

* 🌐 **Live Chatbot UI:**
  https://app-handbook-rag-ai-hcgfmc7nansdzzcnbsmu3c.streamlit.app

* ⚙️ **Backend API (Render):**
  https://gitlab-handbook-rag-ai.onrender.com/docs

---

## 🎯 Objective

Inspired by GitLab's *"build in public"* philosophy, this GenAI chatbot provides an interactive and engaging interface for employees and candidates to access information from GitLab’s Handbook and Direction pages.

It bridges the gap between massive documentation and instant, accessible learning.

---

## 🚀 Key Features

* **Semantic Retrieval**
  Uses vector similarity search to find policy and culture matches based on meaning, not just keywords.

* **Real-time Generation**
  Leverages Gemini for context-aware, human-like responses.

* **Intuitive UI**
  A clean, user-friendly Streamlit interface designed for seamless follow-up questions.

* **Resilient Architecture**
  Basic error handling ensures smooth user interaction during API rate limits.

---

## 🛠️ Tech Stack

* **LLM:** Gemini (via Google AI Studio)
* **Embeddings:** Sentence-Transformers `all-MiniLM-L6-v2`
* **Database:** Supabase (PostgreSQL with `pgvector`)
* **Backend:** FastAPI & Uvicorn
* **Frontend:** Streamlit
* **Deployment:** Render (Backend) & Streamlit Community Cloud (Frontend)

---

## 🏗️ Data Pipeline & Approach

1. **Data Retrieval**
   `scraper.py` crawls and extracts structured text from the GitLab Handbook.

2. **Chunking & Embedding**
   Text is broken into manageable chunks and converted into 384-dimensional vectors.

3. **Vector Storage**
   Metadata and embeddings are stored in Supabase for high-speed similarity search.

4. **RAG Workflow**
   FastAPI backend retrieves relevant context and sends it to the LLM for grounded answers.

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashishjaiswar21/Gitlab-Handbook-RAG-AI.git
cd Gitlab-Handbook-RAG-AI
```

---

### 2. Local Configuration

Create a `.env` file in the root directory:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
GEMINI_API_KEY=your_google_ai_studio_key
```

---

### 3. Running Locally

#### Terminal 1 (Backend)

```bash
python -m uvicorn Gitlab-chatbot.backend.main:app --reload
```

#### Terminal 2 (Frontend)

```bash
streamlit run Gitlab-chatbot/frontend/app.py
```

---

## 💡 Innovation & Bonus Features

* **Microservices Architecture**
  Separate frontend and backend for scalability and better engineering design.

* **Memory Optimization**
  Optimized to run efficiently on free-tier cloud resources.

* **Transparency (Optional)**
  Can include source references in chatbot responses for trust and explainability.

---

## 📌 Future Improvements

* Add user authentication and chat history (Supabase)
* Improve UI with React or advanced Streamlit components
* Add multilingual support

---

## 👨‍💻 Developer

**Ashish Kumar**
B.Tech in Information Technology
Netaji Subhas University of Technology (NSUT) '26

---
