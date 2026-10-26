from langchain_ollama import ChatOllama
from dotenv import load_dotenv

class ModeloLocal2:
    def __init__(self):
        load_dotenv()
        self.modelo = ChatOllama(model="phi4-mini:3.8b", temperature=0.1)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text