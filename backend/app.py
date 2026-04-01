from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
import torch
import os

#  Initialize FastAPI

app = FastAPI()

#  Load LLaMA Model
MODEL_NAME = "meta-llama/Llama-4"  # change if needed

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Model loaded successfully!")

# 🧠 Memory (Chat History)
memory = ConversationBufferMemory()

# 🔍 Embeddings + Vector DB
embedding_model = HuggingFaceEmbeddings()
vector_db = None

#  Request Schema

class ChatRequest(BaseModel):
    query: str
  
#  Chat Function

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

#  Upload Documents (RAG)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global vector_db

    content = await file.read()
    text = content.decode("utf-8")

    # Create vector DB
    vector_db = FAISS.from_texts([text], embedding_model)

    return {"message": "File uploaded and indexed successfully"}

#  Chat Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    global vector_db

    user_query = request.query

    # Retrieve context (RAG)
    context = ""
    if vector_db:
        docs = vector_db.similarity_search(user_query, k=2)
        context = "\n".join([doc.page_content for doc in docs])

    # Combine prompt
    full_prompt = f"""
    Context:
    {context}

    User: {user_query}
    Assistant:
    """

    response = generate_response(full_prompt)

    # Save memory
    memory.save_context({"input": user_query}, {"output": response})

    return {
        "query": user_query,
        "response": response
    }
#  Health Check
@app.get("/")
def root():
    return {"message": "LLaMA Chatbot API is running 🚀"}
