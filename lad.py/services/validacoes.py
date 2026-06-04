def validar_cpf(cpf):
    soma = 0
    soma_2dv = 0
    resto_2dv = 0
    primeiro_dv = 0
    segundo_dv = 0

    if len(cpf) != 11:
        return False
    
    todos_iguais = True
    for i in cpf:
        if i != cpf[0]:
            todos_iguais = False

    if todos_iguais == True:
        return False
    
    if not cpf.isdigit():
        return False

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11 
    if resto < 2:
        primeiro_dv = 0
    else:
        primeiro_dv = 11 - resto
        if primeiro_dv >= 10:
            primeiro_dv = 0

    for i in range(10):
        soma_2dv += int(cpf[i]) * (11 - i)

    resto_2dv = soma_2dv % 11
    if resto_2dv < 2:
        segundo_dv = 0
    else:
        segundo_dv = 11 - resto_2dv
    
    if primeiro_dv != int(cpf[9]) or segundo_dv != int(cpf[10]):
        return False

    return True

def validar_titulo(titulo):
    soma = 0
    titulo_resto_1dv = 0

    if len(titulo) != 12:
        return False
    
    if not titulo.isdigit():
        return False

    for i in range(8):
        soma += int(titulo[i]) * (2 + i)
    
    titulo_resto_1dv = soma % 11
    if titulo_resto_1dv >= 10:
        titulo_1dv = 0
    else:
        titulo_1dv = titulo_resto_1dv

    


