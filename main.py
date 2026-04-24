import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_groq import ChatGroq

load_dotenv()

app = FastAPI()
llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))

@app.get("/")
def read_root():
    return {"status": "running"}

@app.post("/chat")
def chat(prompt: str):
    response = llm.invoke(prompt)
    return {"response": response.content}