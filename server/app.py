from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.analyzer import analyze_test_file

app = FastAPI()

class TestFile(BaseModel):
    content: str

@app.post("/validate")
async def validate_test_file(test_file: TestFile):
    """API to validate test file content."""
    if not test_file.content.strip():
        raise HTTPException(status_code=400, detail="Empty test file provided.")

    issues = analyze_test_file(test_file.content)
    return {"issues": issues}

@app.get("/health")
async def health_check():
    return {"status": "API is running"}
