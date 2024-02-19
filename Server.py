# server.py

import socket, threading

print_lock = threading.Lock()

# le serveur n'as besoin d'adresse car il ne va qu'ecouter
host,port = (('127.0.0.1', 44444))

# on cree le socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# pour se connecter avec une adresse (on associe le socket avec l'adresse)
serverSocket.bind((host, port))
serverSocket.listen(5)
# en lui passe en parametre le nombre de connexion qui peuvent echouer avant de le refuser (facultatif pour py 3.5)
print("Le serveur est en marche sur port " , port)

# créér deux listes vides pour mettre les noms des clients
clients = []
users = []

# Envoyer les messages de chat pour les clients qui sont en connexion 
def broadcast(message):
    # Le client qui nous a envoyer une message dans clients
    for client in clients:
            client.send(message)

def handle(client):
    # on va faire ecouter le serveur sur le port continuellement
    while True:
        # Essayer de broadcast le message si les client l'ont recu
        try:
            message = client.recv(1024)
            broadcast(message)

        except: 
            # On va lui enlever au cas qu'il n'y a pas de connexion 
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[index]
            #chaque fois q'on ajoute un client, on va aussi l'ajouter son index au user
            broadcast(f'{user} a disconnecte du chat!'.encode('utf8'))
            # Message pour le server aussi!
            print(f'{user} a disconnecte du chat!')
            users.remove(user)
            break

def receive():
    while True:
        try:
            # on va initialiser les connexion pour pouvoir les accepter
            conn, address = serverSocket.accept()  # adresse = adresse IP + port

            # pur l'admin sache quelqu'un est venu et on attend, puis
            print("Un client vient de connecter avec" + address[0] + str(address[1]))

            # Pour le client sait quoi taper
            conn.send("TINA".encode('utf8'))
            # on recoit la donner et on decode la donner
            message = conn.recv(1024).decode('utf8')   # la taille de buffer pour receptioner l'info multiple de 2
            users.append(message)
            clients.append(conn)

            # Montrer le user du client
            print("Le user du client est: " + message)
            # Pour savoir qui est arrive
            broadcast(f'{message} a rejoint le chat \n'.encode('utf8'))
            # Pour le client sait qu'il est connecte sur le server
            conn.send('Vous etes connecte au server'.encode('utf8'))
            
            # On va commencer avec le single-threading pour ce client
            thread = threading.Thread(target=handle, args=(conn,))
            thread.start()
        

        except (BrokenPipeError, ConnectionRefusedError) as e:
            print("La connexion au serveur a echoue ", e)
            clients.remove(conn)
            conn.close()
            serverSocket.close()
      
# Recevoir l'info pour le client et le faire courrir
receive()

