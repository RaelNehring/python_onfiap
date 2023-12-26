with open("D:\\[01 Rael Nehring]\\GitHub_RaelNehring\\python_onfiap\\modulo04\\aula02\\arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read() #Leitura de todo o arquivo
    print(conteudo)


arquivo.close()

print("Acesso linha à linha:")
with open("D:\\[01 Rael Nehring]\\GitHub_RaelNehring\\python_onfiap\\modulo04\\aula02\\arquivo.txt", "r") as arquivo:
    #Imprimindo por linha
    for linha in arquivo.readlines():
        print(linha)

arquivo.close()