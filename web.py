from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from main import generate_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummaryRequest(BaseModel):
    choice: str
    text: str
    mode: str

@app.get("/")
def health_check():
    return {"status": "healthy"}

@app.post("/summarize")
def summarize(request: SummaryRequest):
    result = generate_summary(request.choice, request.text, request.mode)
    return {"summary": result}
