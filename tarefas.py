print("Seja bem-vindo ao seu Gerenciador de Tarefas Diárias! Selecione a opção desejada de acordo com o menu.")

def adicionarTarefa(tarefa, novaTarefa):
    tarefa.append(novaTarefa)
    print("Tarefa adicionada com sucesso!")

def visualizarTarefas(tarefa):
    print("Lista de tarefas:")
    for i, tarefas in enumerate(tarefa, start=1):
        print(f"{i}. {tarefas}")

def marcarComoConcluida(tarefa):
    visualizarTarefas(tarefa)
    numeroTarefa = int(input("Digite o número da tarefa concluída: "))
    if 1 <= numeroTarefa <= len(tarefa):
        tarefa.pop(numeroTarefa - 1)
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def removerTarefa(tarefa):
    visualizarTarefas(tarefa)
    numeroTarefa = int(input("Digite o número da tarefa que deseja remover: "))
    if 1 <= numeroTarefa <= len(tarefa):
        tarefa.pop(numeroTarefa - 1)
        print("Tarefa removida com sucesso!")
    else:
        print("Número da tarefa não encontrado.")


tarefa = []
while True:
    print("MENU DE OPÇÕES:")
    print("Para adicionar uma nova tarefa, digite: 1")
    print("Para vizualizar todas as tarefas listadas, digite: 2 ")
    print("Para marcar uma tarefa como concluída, digite: 3 ")
    print("Para remover uma tarefa, digite: 4 ")
    print("Para sair do programa, digite: 5")
    t = input("Escolha uma opção: ")

    if t == "1":
        novaTarefa = input("Digite a nova tarefa: ")
        adicionarTarefa(tarefa, novaTarefa)
    elif t == "2":
        visualizarTarefas(tarefa)
    elif t == "3":
        marcarComoConcluida(tarefa)
    elif t == "4":
        removerTarefa(tarefa)
    elif t == "5":
        print("Saindo...")
        break
    else:
        print("Opção não encontrada.")

    e = input("Deseja continuar? s/n: ")
    if e == "n":
        print("Saindo...")
        break