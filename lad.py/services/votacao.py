import os


def exibir_opcoes():
    os.system('cls')
    print("============================")
    print("1. Abrir sistema de votação")
    print("2. Auditoria da votação")
    print("3. Resultados da votação")
    print("4. Voltar ao menu")
    print("============================")

def votacao():
    exibir_opcoes()

    opcao = int(input("Escolha uma opção: "))
    while opcao != 4 :
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                print("Opção Inválida!")

    sistema_aberto = False
    return sistema_aberto

def resultados_votacao(sistema_aberto):
    if sistema_aberto == False:
        print("O Sistema de Votação ainda não foi aberto, portanto não tem resultados ainda!")
    else:
        pass
    


