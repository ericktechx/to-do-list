# Importando o script view.py
from view import *

# Função principal para interagir com o usuário
def main():
    # Criando Menu
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Excluír tarefa")
        print("5. Sair")

        escolha = input("Digite a escolha (1-5): ")

        if escolha == "1":
            descricao = input("Digite a descrição: ")
            adicionar_tarefas(descricao)
            print("Tarefa adicionada com sucesso!")

        elif escolha == "2":
            tarefas = obter_tarefas()
            if len(tarefas) == 0:
                print("Nenhuma tarefa encontrada.")
            else:
                for tarefa in tarefas:
                    print(f"{tarefa[0]}. {tarefa[1]} - {'Concluida' if tarefa[2] else 'Incompleta'}")

        elif escolha == "3":
            id_tarefa = input("Digite o ID da tarefa: ")
            marcar_completo(id_tarefa)
            print("Tarefa marcada como concluída.")

        elif escolha == "4":
            id_tarefa = input("Digite o ID da tarefa: ")
            deletar_tarefas(id_tarefa)
            print("Tarefa excluída.")

        elif escolha == "5":
            break

        else:
            print("Escolha inválida.")
    meubd.close()


if __name__ == "__main__":
    main()
    