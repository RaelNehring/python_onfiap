tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
"""
range(inicio, fim[, incremento])
inicio=> O primeiro valor do loop
fim=> enquanto não chegar nesse valor, executa (vai executar o que estiver dentro enquanto for MENOR do que 11)
incremento=> A cada passo, irá incrementar neste valor
"""
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))