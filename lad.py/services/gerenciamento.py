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
                print("Funcionalidade em desenvolvimento...")
            case 3:
                remover_eleitor()
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
    try:
        cursor.execute(
            "INSERT INTO eleitor (nome, titulo, cpf, mesario) VALUES (%s, %s, %s, %s)",
            (nome, titulo, cpf, mesario)
        )

        db.commit()
        db.close()
        print("Eleitor cadastrado com sucesso!")

    except:
        print("CPF ou Título já cadastrado!")
    

def listar_eleitor():
    db = cx.conectar()
    cursor = db.cursor()
    cursor.execute(
        "SELECT nome, titulo, cpf, mesario FROM eleitor"
    )
    resultados = cursor.fetchall()
    
    if len(resultados) == 0:
        print("Nenhum eleitor foi cadastrado ainda!")

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
    resposta = input("Digite 'CPF' ou 'T' para Título: ")
    if resposta.lower()  == "cpf":
        cpf_para_buscar = input("Digite o CPF que você quer buscar: ")
        cursor.execute(
            "SELECT * FROM eleitor WHERE cpf = %s",
            (cpf_para_buscar,)
        )
        resultados = cursor.fetchall()
        if cpf_para_buscar in resultados:
            for elemento in resultados:
                print(f"Eleitor: {elemento[1]} | Título: {elemento[2]} | CPF: {elemento[3]} | Mesário: {elemento[4]}")
    elif resposta.lower() == "t":
        titulo_para_buscar = input("Digite o Título que você quer buscar: ")
        cursor.execute(
            "SELECT * FROM eleitor WHERE titulo = %s",
            (titulo_para_buscar,)
        )
        resultados = cursor.fetchall()
        if titulo_para_buscar in resultados:
            for elemento in resultados:
                print(f"Eleitor: {elemento[1]} | Título: {elemento[2]} | CPF: {elemento[3]} | Mesário: {elemento[4]}")

def remover_eleitor():
    db = cx.conectar()
    cursor = db.cursor()
    
    cpf_para_remover = input("Digite o CPF do Eleitor que você deseja remover: ")
    cursor.execute(
        "DELETE FROM eleitor WHERE cpf = %s",
        (cpf_para_remover,)
    )
    db.commit()

    if cursor.rowcount == 0:
        print("Eleitor não encontrado!")
    else:
        print("Eleitor removido com sucesso!")

    db.close()