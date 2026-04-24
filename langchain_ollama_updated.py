from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_ollama import ChatOllama
from pydantic import BaseModel

app = FastAPI()
llm = ChatOllama(model="llama3.2", base_url="http://ollama:11434")

class ChatRequest(BaseModel):
    message: str

def generate_stream(message: str):
    for chunk in llm.stream(message):
        yield chunk.content

@app.post("/chat")
async def chat(req: ChatRequest):
    return StreamingResponse(generate_stream(req.message), media_type="text/plain")