import json
import os

ARQUIVO = "todo.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=2)

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista")
    for i, t in enumerate(tarefas,1):
        status = '[x]' if t['concluida'] else '[]'
        print(f"{i}. {status} {t['descricao']}")

def adicionar_tarefa(tarefas):
    desc = input("Nova tarefa: ").strip()
    if desc:
        tarefas.append({'descricao': desc, 'concluida': False})

def marca_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    idx = int(input("Número de tarefas a marcar/desmarcar: ")) - 1
    if 0 <= idx < len(tarefas):
        tarefas[idx]['concluida'] = not tarefas[idx]['concluida']
    
def remove_tarefas(tarefas):
    mostrar_tarefas(tarefas)
    idx = int(input("Número de tarefas a remover: ")) - 1
    if 0 <= idx < len(tarefas):
        tarefas.pop(idx)

def menu():
    tarefas = carregar_tarefas()
    opções = {
        '1': ('Mostrar tarefas', mostrar_tarefas),
        '2': ('Adicionar tarefa', adicionar_tarefa),
        '3': ('Marcar/desmarcar', marca_tarefa),
        '4': ('Remover tarefa', remove_tarefas),
        '5': ('Sair', None)
    }
    while True:
        print("\n=== Lista de Tarefas ===")
        for k, (txt, _) in opções.items():
            print(f"{k}. {txt}")
        escolha = input("Opção: ")
        if escolha == '5':
            break
        acao = opções.get(escolha)
        if acao:
            acao[1](tarefas)
            salvar_tarefas(tarefas)
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()