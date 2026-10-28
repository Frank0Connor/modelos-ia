from langchain_ollama import ChatOllama
from dotenv import load_dotenv

class Prompt01:
    def __init__(self):
        load_dotenv() 
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.4)

    def generar_respuesta(self):
        respuesta = self.modelo.invoke("Hola, ¿Cómo estás?")
        return respuesta.text