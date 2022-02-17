
verificador_tamanho = False
verificador_digito = False
qntd_digitos = 0
digitos = ['0','1','2','3','4','5','6','7','8','9']
verificador_min = False
verificador_mai = False
verificador_especiais = False  
caractere_especiais = ['!','@','#','$','%','^','&','*','(',')','-','+']

quebra_loop = ''
while quebra_loop == '':
    senha = input("digite sua senha: ")
    tamanho_senha = len(senha)
    ## Verificando a quantidade de caracteres
    if tamanho_senha < 6:
     print("A senha não satisfaz o número mínimo de caracteres, digite mais", + 6 - tamanho_senha , "caracteres para corrigir.") 
     verificador_tamanho = True
    ## Verificando se há pelo menos 1 numero
    for i in senha:
        for y in digitos:
            if i == y:
                verificador_digito = True 
    if verificador_digito == False:
        print('Sua senha tem que ter pelo menos 1 digito.')
    ## Verificando se há pelo menos 1 letra maiúsculo
    if senha.upper() != senha:
        verificador_min = True
    if verificador_min == False:
        print("Sua senha tem que ter pelo menos 1 letra maiúsculo.")
    ## Verificando se há pelo menos 1 letra minúscula
    if senha.lower() != senha:
        verificador_mai = True
    if verificador_mai == False:
        print("Sua senha tem que ter pelo menos 1 letra minúscula.")
    ## verificando se há pelo menos 1 caractere especial    
    for x in senha:
        for z in caractere_especiais:
            if x == z:
                verificador_especiais = True
    if verificador_especiais == False:
        print("Sua senha tem que ter pelo menos 1 caractere especial.")
    ## caso a senha esteja certa
    if verificador_min and verificador_digito and verificador_especiais and verificador_tamanho and verificador_mai == True:
        print("Senha cadastrada com sucesso.")
        quebra_loop = input("Digite qualquer tecla para finalizar.")
