from dados import usuarios

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(usuario)
    print(f"Usuário cadastrado com sucesso! Bem-vindo, {nome}!")

def logar_usuario():
    
    while True:
        email = input("Digite seu email: ")
        encontrado = False
        senha_correta = False
        for usuario in usuarios:
            if email == usuario["email"]:
                print("Email encotrado!")
                encontrado = True
                senha = input("digite sua senha: ")
                if senha != usuario["senha"]:
                    print("Senha incorreta! Tente novamente ")
                elif senha == usuario["senha"]:
                    print("Conta logada com sucesso! ")
                    senha_correta = True
        if senha_correta == True:
            break
        elif encontrado == False:
            print("Email não encontrado! ")