import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")#Faz com que a senha não seja exibida enquanto é digitada

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")