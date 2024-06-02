import socket
import threading

# Créer une socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier la socket à une adresse et un port spécifiques
server_address = ('localhost', 12345)
sock.bind(server_address)

# Écouter les connexions entrantes (avec un maximum de 5 connexions en attente)
sock.listen(5)

def handle_client(client_socket):
    # Afficher une notification lorsqu'un nouveau client se connecte
    print('Nouvelle connexion depuis ', client_address)

    try:
        # Recevoir les données envoyées par le client
        message = client_socket.recv(1024).decode()

        while message:
            # Afficher le message reçu
            print('Message reçu : ', message)

            # Recevoir les données suivantes envoyées par le client
            message = client_socket.recv(1024).decode()

    finally:
        # Fermer la connexion avec le client
        client_socket.close()

while True:
    # Accepter une nouvelle connexion entrante
    print('En attente d\'une connexion...')
    client_socket, client_address = sock.accept()

    # Créer un nouveau thread pour gérer la connexion avec le client
    t = threading.Thread(target=handle_client, args=(client_socket,))
    t.start()
