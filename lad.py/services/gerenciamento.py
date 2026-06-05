from db import conexao as cx
from services import validacoes as vd
import os

def exibir_opcoes():
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

def gerenciamento():
    exibir_opcoes()
    
    opcao = int(input("Escolha uma opção: "))
    while opcao != 7:
        match opcao:
            case 1:
                cadastrar_eleitor()
            case 2:
                pass
            case 3:
                pass
            case 4:
                buscar_eleitor()
            case 5:
                listar_eleitor()
            case 6:
                pass
            case _:
                print("Opção Inválida!")
        
        exibir_opcoes()
        opcao = int(input("Escolha uma opção: "))

def cadastrar_eleitor():
    nome = input("Por favor, digite seu nome completo: ")
    
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
        "INSERT INTO eleitor (nome, titulo, cpf, mesario) VALUES (%s, %s, %s, %s)",
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
        mesario = ""
        if eleitor[3] == "S":
            mesario = "Sim"
        else:
            mesario = "Não"
        print(f"Eleitor: {eleitor[0]} | Título: {eleitor[1]} | CPF: {eleitor[2]} | Mesário: {mesario}")
        

    db.close()
    input("Aperte qualquer tecla para voltar ao menu: ")

def buscar_eleitor():
    db = cx.conectar()
    cursor = db.cursor()

    print("Você quer buscar por CPF ou por Título de Eleitor? ")
    resposta = input("Digite 'CPF' ou 'Titulo': ")
    if resposta  == "CPF":
        cpf_para_buscar = input("Digite o CPF que você quer buscar: ")
        cursor.execute(
            "SELECT * FROM eleitor WHERE cpf = %s",
            (cpf_para_buscar,)
        )
        resultados = cursor.fetchall()
        for elemento in resultados:
            print(f"Eleitor: {elemento[0]} | Título: {elemento[1]} | CPF: {elemento[2]} | Mesário: {elemento[3]}")