# pip install langchain_ollama
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

class ModeloLocal:
    def __init__(self):
        load_dotenv()
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text