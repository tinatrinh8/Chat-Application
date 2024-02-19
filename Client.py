# client.py

import socket, threading

# On va passer aussi une chance pour le client pour inscrire son user
user = input("Choisi ton user: ")
# on cree le socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set l'adresse et e port pour communiquer avec le serveur
host, port = (('127.0.0.1', 44444))


clientSocket.connect((host,port))

def receive():
    while True:
        try:
            # On va faire sur que le nom/user du client est correcte par le server.
            message = clientSocket.recv(1024).decode('utf8')
            if message == 'TINA':
                clientSocket.send(user.encode('utf8'))
               # Sinon, on va juste imprimer le message directement juste au cas ou le server l'a recu seulement.
            else:
                print(message)
                    
        except (ConnectionResetError, ConnectionRefusedError): 
            print("La connexion au serveur a echoue ")
            clientSocket.close()
            break

def write():
    while True:
        # Il faut encoder l'informaton avant de l'envoyer
        message = f'{user}: {input("")}'
        # on envoie l'information
        clientSocket.send(message.encode('utf8'))

receive = threading.Thread(target=receive)
receive.start()
write = threading.Thread(target=write)
write.start()



