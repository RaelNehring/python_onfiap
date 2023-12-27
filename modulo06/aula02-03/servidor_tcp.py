from socket import *

servidor = "127.0.0.1" # Endereço IP do servidor (localhost)
porta = 43210 # Porta de entrada para poder acessar

"""
Instanciando objeto socket
AF_INET => Identificação por IP ou Hostname
SOCK_STREAM => Para poder trabalhar com o protocolo TCP
"""
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2) # Quantidade máximas de clientes que a aplicação vai poder ter simultaneamente

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()