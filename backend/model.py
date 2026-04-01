from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
import torch

#  Model Configuration
MODEL_NAME = "meta-llama/Llama-4"  # change if needed

print("🔄 Loading LLaMA model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("✅ Model loaded successfully!")

#  Memory (Chat History)

memory = ConversationBufferMemory()

#  Embeddings + Vector DB

embedding_model = HuggingFaceEmbeddings()
vector_db = None


#  Create Vector DB

def create_vector_db(texts):
    global vector_db
    vector_db = FAISS.from_texts(texts, embedding_model)

#  Retrieve Context (RAG)
def get_context(query):
    global vector_db

    if vector_db is None:
        return ""

    docs = vector_db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in docs])

#  Generate Response

def generate_response(query):
    context = get_context(query)

    prompt = f"""
    Context:
    {context}

    User: {query}
    Assistant:
    """

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.7,
        do_sample=True,
        top_p=0.9
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Save memory
    memory.save_context({"input": query}, {"output": response})

    return response
