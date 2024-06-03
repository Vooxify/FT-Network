import threading
from common.context import Context

context = Context()


# Global

def handle_client(client_socket):

    try:
        message = client_socket.recv(1024).decode()
        while message:
            message = client_socket.recv(1024).decode()
            print(message)

    finally:
        client_socket.close()

def start_server():

    # FOR DEV REMOVE IF YOU USE !!
    context.set("IP", "localhost")

    sock = context.get("SOCKET")
    print(context.get("IP"), context.get("PORT"))
    sock.bind((context.get("IP"), context.get("PORT")))
    sock.listen()
    while True:
        client_socket, client_address = sock.accept()

        t = threading.Thread(target=handle_client, args=(client_socket,))
        t.start()
