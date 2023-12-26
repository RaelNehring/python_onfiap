"""
Manipulando Strings com Python
"""

texto = "Leia e Han Solo"

print(texto[0:4])# Partindo de 0, pega 4 posições
print(texto[7:])# Partindo da posição 7 até o final

print(texto.__len__()) # Este é o tamanho da string. É por ele que começamos a contar as posições de trás pra frente
print(texto[-8:])#Com sinal negativo, representa a posição de trás pra frente]

print(texto[::-1])# Print ao inverso

# Posição Inicial : qtde de posições à percorrer : passo(percorre de n em n)
print(texto[0:4:2])