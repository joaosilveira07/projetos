from db import conexao as cx
from services import validacoes as vd
import os

def gerenciamento():
    os.system('cls')
    print("===============================")
    print("1. Cadastrar Eleitor")
    print("2. Editar Eleitor")
    print("3. Remover Eleitor")
    print("4. Buscar Eleitor")
    print("5. Listagem de Eleitores")
    print("6. Gerenciamento de Candidatos")
    print("7. Voltar ao menu")
    print("===============================")

    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            cadastrar_eleitor()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            listar_eleitor()
        case 6:
            pass
        case 7:
            return
        case _:
            print("Opção Inválida!")

def cadastrar_eleitor():
    nome = input("Por favor, digite seu nome completo.")
    
    titulo = input("Por favor, digite seu título de eleitor (apenas números): ")
    while vd.validar_titulo(titulo) != True:
        print("Título Inválido! Por favor, tente novamente!")
        titulo = input("Por favor, digite seu título de eleitor (apenas números): ")

    cpf = input("Por favor, digite seu CPF (apenas números): ")
    while vd.validar_cpf(cpf) != True:
        print("CPF Inválido! Por favor, tente novamente!")
        cpf = input("Por favor, digite seu CPF (apenas números): ")

    mesario = input("Você atuará como mesário? (S/N): ")

    

    db = cx.conectar()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO eleitor (nome, titulo, cpf, mesario) VALUES %s %s %s %s",
        (nome, titulo, cpf, mesario)
    )
    db.commit()
    db.close()
    print("Eleitor cadastrado com sucesso!")
    

def listar_eleitor():
    db = cx.conectar()
    cursor = db.cursor()
    cursor.execute(
        "SELECT nome, titulo, cpf, mesario FROM eleitor"
    )
    resultados = cursor.fetchall()
    for eleitor in resultados:
        print(f"Eleitor: {eleitor[0]} | Título: {eleitor[1]} | CPF: {eleitor[2]} | Mesário: {eleitor[3]}")

    db.close()
