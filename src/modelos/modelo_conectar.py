from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Prompt_Conexion:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuesta(self):

        plantilla = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                Eres un profesor universitario de programación

                Instrucciones:
                - Responde siempre en español.
                - Utiliza lenguaje sencillo.
                - Incluye un ejemplo en Python.
                - No utilices tecnicismos innecesarios.
                """
            ),
            (
                "human",
                "Explícame el siguiente tema: {tema}"
            )
        ])

        cadena = plantilla | self.modelo | StrOutputParser()

        mensajes = cadena.invoke({
            "tema": "estructuras repetitivas"
        })

        respuesta = self.modelo.invoke(mensajes)

        return respuesta.content