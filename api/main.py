from fastapi import FastAPI, Request
from rag_core import get_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    return get_answer(query)

# ✅ Vercel needs this for ASGI support
handler = app
