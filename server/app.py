import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Ensure the script can find the 'agent' module
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

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
