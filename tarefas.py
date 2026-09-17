import json
import requests

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)


def mostrar_menu():
    print("\n--- MINHAS TAREFAS ---")
    print("1 - Listar tarefas")
    print("2 - Criar tarefa")
    print("3 - Marcar tarefa como feita")
    print("4 - Apagar tarefa")
    print("5 - Sair")

def listar(tarefas):
    if not tarefas:
        print("Nehuma tarefa ainda")
        return
    for i, tarefa in enumerate(tarefas):
        if tarefa["feita"] == True:
            status = "✅"
        else:
            status = "❌"
        print(f"{i} - {status} {tarefa['titulo']}")


def buscar_frase_motivacional():
    try:
        resposta = requests.get("https://api.adviceslip.com/advice")
        dados = resposta.json()
        return dados["slip"]["advice"]
    except requests.exceptions.RequestException:
        return "Continue assim, um passo de cada vez!"


tarefas = carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        listar(tarefas)

    elif opcao == "2":
        titulo = input("Título da tarefa: ")
        tarefas.append({"titulo": titulo, "feita": False})
        salvar_tarefas(tarefas)
        print("Tarefa criada!")

    elif opcao == "3":
        listar(tarefas)
        indice = int(input("Número da tarefa a marcar como feita: "))
        tarefas[indice]["feita"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como feita!")
        print(buscar_frase_motivacional())

    elif opcao == "4":
        listar(tarefas)
        indice = int(input("Número da tarefa a apagar: "))
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("Tarefa apagada!")

    elif opcao == "5":
        print("\nTenha um Bom Dia.")
        print("Até mais!\n")  
        break

    else:
        print("Opção inválida.")