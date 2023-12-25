inventario=[]
resposta="S"

while resposta=="S":
  inventario.append(input("Equipamento: ")) # a função .append adiciona o item no final da lista
  inventario.append(float(input("Valor: ")))
  inventario.append(input("Número Serial: "))
  inventario.append(input("Departamento: "))
  resposta = input('Digite "S" para continuar: ').upper()

# Percorre a lista para printar os elementos
for elemento in inventario:
  print(elemento)