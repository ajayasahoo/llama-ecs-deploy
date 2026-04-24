import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_openai import ChatOpenAI

load_dotenv()

app = FastAPI()
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def read_root():
    return {"status": "running"}

@app.post("/chat")
def chat(prompt: str):
    response = llm.invoke(prompt)
    return {"response": response.content}