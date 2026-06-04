def validar_cpf(cpf):
    soma = 0

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
