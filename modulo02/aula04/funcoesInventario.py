# Função para preencher o inventário
def preencherInventario(lista):
  resp="S"
  while resp  ==  "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              input("Número Serial: "),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input('Digite "S" para continuar: ').upper()

# Função para exibir os itens do inventário
def exibirInventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# Função para localizar o equipamento por nome
def localizarPorNome(lista):
  busca = input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca == elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

# Função para decrementar o valor do equipamento em 10%
def depreciarPorNome(lista, porc):
  depreciacao = input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao == elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])

# Função para excluir o elemento da lista através do serial
def excluirPorSerial(lista):
  serial = input("Digite o serial do equipamento que será excluido: ")
  for elemento in lista:
    if elemento[2] == serial:
      lista.remove(elemento)
  return "Itens excluídos."

# Função para resumir os valores do inventário
def resumirValores(lista):
  valores = []
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))