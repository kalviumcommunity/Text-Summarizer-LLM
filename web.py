from fastapi import FastAPI
from pydantic import BaseModel
from main import generate_summary

app = FastAPI()

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
