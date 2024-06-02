import socket
import time

# Créer une socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur à une adresse et un port spécifiques
server_address = ('localhost', 12345)
sock.connect(server_address)

try:
    # Envoyer des messages en continu au serveur toutes les secondes
    while True:
        message = input("Bababoi : ")
        sock.sendall(message.encode())
        time.sleep(1)

finally:
    # Fermer la connexion avec le serveur
    sock.close()
