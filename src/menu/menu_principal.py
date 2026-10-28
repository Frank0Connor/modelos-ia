from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_local import ModeloLocal
from src.modelos.modelo_local2 import ModeloLocal2
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt02
from src.modelos.modelo_roles import Prompt03

import os
from rich.console import Console
from rich.markdown import Markdown

class menuPrincipal():
    def __init__(self):
        self.console = Console()
        self.opcion = ""

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresione Enter para volver al menu...")

    def mostrar_menu(self):
        print("=== Menú Principal ===\n")
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local (Ollama)")
        print("4. Modelo Local 2 (Ollama)")
        print("5. Prompt básico")
        print("6. Prompt avanzado")
        print("7. Prompt con roles")
        print("8. Prompt conexión")
        print("\n0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("\n> Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoogle()
                prompt = input("\n> Ingrese su prompt: ")
                respuesta = modelo_google.generar_respuesta(prompt)
                print("\nRespuesta del modelo Google:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown
    
            elif self.opcion == "2":
                modelo_groq=ModeloGroq()
                prompt=input("\n> Ingrese su prompt: ")
                respuesta=modelo_groq.generar_respuesta(prompt)
                print("\nRespuesta del modelo Groq:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "3":
                modelo_local = ModeloLocal()
                prompt = input("\n> Ingrese su prompt: ")
                respuesta = modelo_local.generar_respuesta(prompt)
                print("\nRespuesta del modelo Local:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "4":
                modelo_local2 = ModeloLocal2()
                prompt = input("\n> Ingrese su prompt: ")
                respuesta = modelo_local2.generar_respuesta(prompt)
                print("\nRespuesta del modelo Local 2:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "5":
                prompt01 = Prompt01()
                respuesta = prompt01.generar_respuesta()
                print("\nRespuesta del Prompt básico:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "6":
                prompt02 = Prompt02()
                respuesta = prompt02.generar_respuesta()
                print("\nRespuesta del Prompt avanzado:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "7":
                prompt_roles = Prompt03()
                respuesta = prompt_roles.generar_respuesta()
                print("\nRespuesta del Prompt avanzado:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "8":
                prompt_roles = Prompt03()
                respuesta = prompt_roles.generar_respuesta()
                print("\nRespuesta del Prompt avanzado:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            self.pausar()
