from dados import usuarios

def cadastrar_usuario():

    while True:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")

        email_repetido = False

        for usuario in usuarios:

            if email == usuario["email"]:
                print("Email já cadastrado! Tente novamente")
                email_repetido = True
        
        if email_repetido == False:
            senha = input("Digite a senha do usuário: ")

            usuario = {
                "nome": nome,
                "email": email,
                "senha": senha,
                "saldo": 0
            }

            usuarios.append(usuario)
            print(f"Usuário cadastrado com sucesso! Bem-vindo, {nome}!")
            break

def logar_usuario():
    
    while True:
        email = input("Digite seu email: ")
        encontrado = False

        for usuario in usuarios:

            if email == usuario["email"]:
                print("Email encotrado!")
                encontrado = True
                senha = input("digite sua senha: ")
                if senha != usuario["senha"]:
                    print("Senha incorreta! Tente novamente ")
                elif senha == usuario["senha"]:
                    print("Conta logada com sucesso! ")
                    return usuario

        if encontrado == False:
            print("Email não encontrado! ")