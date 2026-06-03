import gerenciamento as gr
import os

def exibir_opcoes():
    os.system('cls')
    print("=====================")
    print("1. Gerenciamento")
    print("2. Votação")
    print("3. Finalizar sistema.")
    print("=====================")

def finalizar():
    input("Aperte qualquer tecla para encerrar o sistema: ")
    print("Encerrando sistema...")

def escolher_opcao():
    opcao = int(input("Escolha uma opção: "))
    while opcao != 3:
        match opcao:
            case 1:
                gr.gerenciamento()
            case 2:
                pass
            case _:
                print("Opção Inválida!")

        exibir_opcoes()
        opcao = int(input("Escolha uma opção: "))

    finalizar()

def main():
    os.system('cls')
    try:
        exibir_opcoes()
        escolher_opcao()
    except:
        print("Opção Inválida!")

main()