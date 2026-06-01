from funcoes import cadastrar_usuario
from funcoes import logar_usuario

def menu_principal():
    while True:

        print("Bem vindo ao menu de opções! Escolha uma opção:")

        print(" 1 - cadastrar usuário")
        print(" 2 - logar usuário")
        print(" 3 - sair do programa")
    
        escolha_usuario = int(input("Digite o número da opção desejada: "))
        if escolha_usuario == 1:
            cadastrar_usuario()
        elif escolha_usuario == 2:
            logar_usuario()
        elif escolha_usuario == 3:
            print("Saindo do programa. Até mais!")
            break