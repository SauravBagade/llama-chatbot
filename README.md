# 🤖 LLaMA Chatbot (FastAPI + RAG + DevOps Ready)

A **production-ready AI chatbot** built using **LLaMA (open-source LLM)**, **FastAPI**, and **LangChain**, with support for **RAG (Retrieval-Augmented Generation)** and **DevOps deployment (Docker/Kubernetes)**.

---

# 📌 🚀 Project Overview

This project allows you to:

* 💬 Chat with LLaMA model
* 📄 Upload documents and ask questions (RAG)
* 🧠 Maintain chat memory
* 🌐 Use a simple Bootstrap frontend
* 🐳 Deploy using Docker
* ☸️ Scale using Kubernetes (optional)

---

# 🏗️ 🧠 Architecture

```
Frontend (HTML/Bootstrap)
        ↓
FastAPI Backend (app.py)
        ↓
Model Layer (model.py)
        ↓
LLaMA Model + LangChain
        ↓
FAISS Vector DB (RAG)
```

---

# 📁 📂 Project Structure

```
llama-chatbot/
│
├── app.py                # FastAPI backend
├── model.py              # LLaMA + RAG logic
├── requirements.txt      # Dependencies
├── Dockerfile            # Container setup
│
├── frontend/
│   └── index.html        # Chat UI
│
└── README.md             # Documentation
```

---

# ⚙️ 🧰 Requirements

## 💻 System Requirements

| Component | Minimum  | Recommended  |
| --------- | -------- | ------------ |
| RAM       | 8 GB     | 16–32 GB     |
| CPU       | i5       | i7 / Ryzen 7 |
| GPU       | Optional | 8–24 GB VRAM |

---

# 🧪 🔧 Step-by-Step Setup

---

## 🥇 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/llama-chatbot.git
cd llama-chatbot
```

---

## 🥈 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Activate:

**Linux / Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

## 🥉 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Step 4: Hugging Face Login (Required)

```bash
huggingface-cli login
```

👉 Paste your Hugging Face token

---

## 🚀 Step 5: Run Backend Server

```bash
uvicorn app:app --reload
```

👉 Open:

```
http://127.0.0.1:8000/docs
```

---

## 💬 Step 6: Test Chat API

### POST `/chat`

```json
{
  "query": "What is Docker?"
}
```

---

## 📄 Step 7: Upload File (RAG)

### POST `/upload`

* Upload `.txt` file
* Then ask questions related to that file

---

## 🌐 Step 8: Run Frontend

Open:

```
frontend/index.html
```

OR use Live Server (VS Code)

---

# 🐳 🐳 Docker Setup

---

## 🔨 Build Docker Image

```bash
docker build -t llama-chatbot .
```

---

## ▶️ Run Container

```bash
docker run -p 8000:8000 llama-chatbot
```

👉 Open:

```
http://localhost:8000/docs
```

---

# ☸️ Kubernetes Deployment (Optional)

---

## 🧾 Create Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llama-chatbot
spec:
  replicas: 1
  selector:
    matchLabels:
      app: chatbot
  template:
    metadata:
      labels:
        app: chatbot
    spec:
      containers:
      - name: chatbot
        image: llama-chatbot
        ports:
        - containerPort: 8000
```

---

## 🚀 Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

---

# 🔥 Features

* ✅ LLaMA Open-source LLM
* ✅ FastAPI backend
* ✅ LangChain integration
* ✅ FAISS vector database
* ✅ File upload (RAG)
* ✅ Chat memory
* ✅ Bootstrap UI
* ✅ Docker support
* ✅ Kubernetes ready

---

# ⚡ API Endpoints

| Endpoint  | Method | Description     |
| --------- | ------ | --------------- |
| `/`       | GET    | Health check    |
| `/chat`   | POST   | Chat with bot   |
| `/upload` | POST   | Upload file     |
| `/reset`  | POST   | Reset vector DB |

---

# 🧠 Example Use Cases

* 📘 DevOps Assistant (Docker, Kubernetes help)
* 📄 PDF/Text Q&A chatbot
* 🏢 Company internal knowledge bot
* 🎓 Study assistant

---

# ⚠️ Common Issues & Fixes

---

## ❌ Model Not Loading

✔ Solution:

```bash
huggingface-cli login
```

---

## ❌ FAISS Error

```bash
pip install faiss-cpu --no-cache-dir
```

---

## ❌ Slow Performance

✔ Use smaller model:

```python
meta-llama/Llama-3-8b-instruct
```

---

# 🔮 Future Improvements

* 🔄 Streaming responses (like ChatGPT)
* 🔐 Authentication system
* 🗄️ MongoDB chat history
* 🎤 Voice chatbot
* 🌙 Dark mode UI

---

# 👨‍💻 Author

**Saurav Bagade**
DevOps Engineer | AI Enthusiast

---
