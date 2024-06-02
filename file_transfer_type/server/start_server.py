import socket
import threading

from common.context import Context

context = Context()

print(context.get("IP"), context.get("PORT"))

# Global
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add = (context.get("IP"), context.get("PORT"))

sock.bind(add)
sock.listen()

def handle_client(client_socket):
    # Afficher une notification lorsqu'un nouveau client se connecte
    print("[+]  New connection.")

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

def start_server():
    while True:
        print("[+]  Waiting connection.")
        client_socket, client_address = sock.accept()

        t = threading.Thread(target=handle_client, args=(client_socket,))
        t.start()
