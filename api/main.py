from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    return get_answer(query)
