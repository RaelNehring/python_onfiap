inventario=[]
resposta = "S"
while resposta  ==  "S":
  equipamento=[input("Equipamento: "),
               float(input("Valor: ")),
               input("Número Serial: "),
               input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input('Digite "S" para continuar: ').upper()

# Listando todos os equipamentos do inventário
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

# Questionando qual elemento o usuário gostaria de visualizar (pelo nome)
busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca == elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

# Questiona qual equipamento o usuário gostaria de reduzir o valor em 10%
depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao == elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

# Questiona e remove o equipamento pelo serial
serial = input("Digite o serial do equipamento que será excluído: ")
for elemento in inventario:
  if elemento[2] == serial:
    inventario.remove(elemento) # A função remove é a responsável por remover o item da lista

# Printando todos os equipamentos
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

# Resumo de valores do inventário
valores=[]
for elemento in inventario:
  valores.append(elemento[1]) #Adicionando todos os valores dentro de outra lista
if len(valores) > 0:
  print("O equipamento mais caro custa: ", max(valores)) # Buscando pelo maior valor
  print("O equipamento mais barato custa: ", min(valores)) # Buscando pelo menor valor
  print("O total de equipamentos é de: ", sum(valores)) # Calculando a soma de todos os equipamentos