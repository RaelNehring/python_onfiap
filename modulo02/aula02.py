"""
Neste caso será criada uma lista para cada valor inserido.
O índice dessa lista irá representar a "PK/IDENTIFICADOR" do item.
"""

# Lista dos valores à serem armazenados
equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = "S"

while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(input("Número Serial: "))
  departamentos.append(input("Departamento: "))
  resposta = input('Digite "S" para continuar: ').upper()

# Printando os itens pelo índice
for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])