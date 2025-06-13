from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from rag_core import get_answer

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all. For production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static frontend files from /public
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# Chat endpoint
@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    response = get_answer(query)
    return JSONResponse(content=response)

# Vercel compatibility
handler = app
