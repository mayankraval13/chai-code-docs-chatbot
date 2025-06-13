from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from rag_core import get_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    result = get_answer(query)
    return JSONResponse(content=result)

# Required for Vercel
handler = app
