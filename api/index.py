from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from rag_core import get_answer

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/public", StaticFiles(directory="public", html=True), name="public")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    return get_answer(query)

# Required for Vercel compatibility
handler = app
