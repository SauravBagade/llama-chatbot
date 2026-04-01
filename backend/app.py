from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Import from model.py
from model import generate_response, create_vector_db


#  Initialize FastAPI App
app = FastAPI(
    title="LLaMA Chatbot API",
    description="FastAPI backend for LLaMA chatbot with RAG",
    version="1.0.0"
)

# -------------------------------
#  Enable CORS (Frontend Access)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
#  Request Schema
# -------------------------------
class ChatRequest(BaseModel):
    query: str

# -------------------------------
#  Health Check
# -------------------------------
@app.get("/")
def root():
    return {
        "status": "success",
        "message": "🚀 LLaMA Chatbot API is running"
    }

# -------------------------------
#  Chat Endpoint
# -------------------------------
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        user_query = request.query.strip()

        if not user_query:
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        response = generate_response(user_query)

        return {
            "query": user_query,
            "response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
#  Upload File (RAG)
# -------------------------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".txt"):
            raise HTTPException(
                status_code=400,
                detail="Only .txt files are supported"
            )

        content = await file.read()
        text = content.decode("utf-8")

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="File is empty"
            )

        # Create vector DB
        create_vector_db([text])

        return {
            "status": "success",
            "message": f"File '{file.filename}' uploaded & indexed"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
#  Optional: Clear Vector DB
# -------------------------------
@app.post("/reset")
def reset():
    try:
        create_vector_db([])  # reset
        return {"message": "Vector DB reset successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
#  Run App (Local Dev)
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
