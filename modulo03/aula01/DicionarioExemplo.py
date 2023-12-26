# Sempre que for criar uma lista ou dicionário, deixar o nome no plural
usuarios = {} # Instanciando o dicionário

usuarios = {"chaves": ["Chaves do 8","24/12/2017","Recep_01"],
            "quico": ["Quico das flores", "20/12/2017","Raiox_03"]
}

print(usuarios)

# Inserindo mais um item no dicionário
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]

print("\nApós inserir a Dona Florinda: ")
print(usuarios)

print("\n Acessando o dicionário por uma chave específica:")
print(usuarios.get("quico"))