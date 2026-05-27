print("Bem vindo ao menu de opções! Escolha uma opção:")
print(" 1 - cadastrar usuário")
print(" 2 - logar usuário")
print(" 3 - sair do programa")

while True:
    escolha_usuario = int(input("Digite o número da opção desejada: "))
    if escolha_usuario == 1:
        input("Digite seu email: ")
        input("Digite sua senha: ")
        print("Usuário cadastrado com sucesso!")
    elif escolha_usuario == 2:
        input("Digite seu email: ")
        input("Digite sua senha: ")
        print("Login realizado com sucesso!")
    elif escolha_usuario == 3:
        print("Saindo do programa. Até mais!")
        break