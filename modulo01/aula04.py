nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()

"""Enquanto a informação for diferente do esperado, faça..."""
while doenca_infectocontagiosa!="SIM" and  doenca_infectocontagiosa!="NAO":
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? (SIM\NÃO)").upper()

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")