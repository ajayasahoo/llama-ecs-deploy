
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    base_url="http://ollama:11434"
)
response = llm.invoke("Explain Docker like I'm 5")
print(response.content)
print(llm.invoke("Tell me a joke").content)
