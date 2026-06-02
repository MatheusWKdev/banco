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
            usuario_logado = logar_usuario()
            menu_conta(usuario_logado)
            break
        elif escolha_usuario == 3:
            print("Saindo do programa. Até mais!")
            break

def menu_conta(usuario_logado):
    while True:
        print("=== Conta Bancária ===")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Logout")
        
        escolha_usuario = int(input("Digite o número da opção desejada: "))

        if escolha_usuario == 1:
            print(f"R${usuario_logado['saldo']}")
        elif escolha_usuario == 2:
            deposito = int(input("Insira o valor do depósito: "))
            if deposito > 0:
                usuario_logado['saldo'] += deposito
                print(f"Depositado com sucesso! Seu saldo agora é de: R${usuario_logado['saldo']}")
            else:
                print("Valor inválido! Digite um valor maior que zero.")

        elif escolha_usuario == 3:
            saque = int(input("Insira o valor do saque: "))
            if saque > 0:
                if saque > usuario_logado['saldo']:
                    print("Saldo insuficiente")
                elif saque <= usuario_logado['saldo']:
                    usuario_logado['saldo'] -= saque
                    print(f"Saque realizado com sucesso! Seu saldo agora é de: R${usuario_logado['saldo']}")
            else:
                print("Valor inválido! Digite um valor maior que zero.")
        elif escolha_usuario == 4:
            print("Saindo do menu da conta. Até mais!")
            break