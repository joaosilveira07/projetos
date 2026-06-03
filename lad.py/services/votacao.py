import os

def votacao():
    os.system('cls')
    print("============================")
    print("1. Abrir sistema de votação")
    print("2. Auditoria da votação")
    print("3. Resultados da votação")
    print("4. Voltar ao menu")
    print("============================")

    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return
        case _:
            print("Opção Inválida!")