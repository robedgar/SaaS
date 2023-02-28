from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()
MAX_INPUT_LENGTH = 32


@app.get("/generate-snippet")
async def generate__snippet_api(prompt: str):
    validate_input_length (prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}

@app.get("/generate-keywords")
async def generate__keywords_api(prompt: str):
    validate_input_length (prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}

@app.get("/generate-snippet_and_keywords")
async def generate__keywords_api(prompt: str):
    validate_input_length (prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.")
    pass

