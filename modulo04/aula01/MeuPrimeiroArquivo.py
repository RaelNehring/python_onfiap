"""
# Criando o arquivo
# Pode-se informar também o diretório onde deverá ser salvo o arquivo, junto ao seu nome

r => Leitura
w => Escrita
a => Ler e Gravar (ótimo para arquivo de log)
x => Abre como 'exclusivo', impedindo que outras pessoas utilizem esse arquivo até o arquivo seja fechado
"""
# Quando utilizamos o parâmetro w, repare que o arquivo sempre será sobrescrevido
with open("primeiro_arquivo_w.txt", "w") as arquivo:
    #Escrevendo no arquivo
    arquivo.write("Meu primeiro arquivo.")
    #Fechando arquivo
    arquivo.close()
# Já utilizando a, irá abrir e incluir o texto
with open("primeiro_arquivo_a.txt", "w") as arquivo:
    #Escrevendo no arquivo
    arquivo.write("Meu primeiro arquivo.")
    #Fechando arquivo
    arquivo.close()

