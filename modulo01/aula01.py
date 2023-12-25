"""
Para declaração de variáveis, deve-se seguir o seguinte padrão:
    nome_usuario
    ou
    nomeUsuario

Os três tipos de dados usados são:
str => String
int => Númerico inteiro
float => Numérico de ponto flutuante
"""
nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))

print()
print(nome + " trabalha na empresa " + empresa) # Forma convencional de concatenar string
print(f"Possui {qtde_funcionarios} funcionarios.")# Também é possível concatenar dessa forma
print(f"A média da mensalidade é de: {str(mediaMensalidade)}")

print("\n==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))