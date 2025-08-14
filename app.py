# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import summarize_text

app = FastAPI(title="Gemini Text Summarizer")

# Request model
class SummarizeRequest(BaseModel):
    text: str
    summary_type: str = "short"  # optional: "short" or "detailed"

# Health check
@app.get("/")
def health_check():
    return {"status": "running", "message": "Gemini Summarizer API is live"}

# Summarization endpoint
@app.post("/summarize")
def summarize(req: SummarizeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    try:
        summary = summarize_text(req.text, req.summary_type)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn app:app --reload
