from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .llm_api import get_answer
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI(title="GitLab Handbook Chatbot API")

# Add CORS middleware so your frontend can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data structure for the request
class ChatRequest(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "GitLab Chatbot API is running!"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        # Call the brain you just built!
        answer = get_answer(request.question)
        return {"question": request.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)