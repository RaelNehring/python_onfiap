def perguntar():
    return input("<I> - Para Inserir um usuário" +
            "\n<P> - Para Pesquisar um usuário" +
            "\n<E> - Para Excluir um usuário" +
            "\n<L> - Para Listar um usuário " +
            "\nO que deseja realizar? ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(), input("Digite a última data de acesso: "), input("Qual a última estação acessada: ").upper()]