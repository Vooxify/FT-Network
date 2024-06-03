import threading
from common.context import Context

context = Context()


# Global

def start_server():

    # FOR DEV REMOVE IF YOU USE !!
    context.set("IP", "localhost")

    sock = context.get("SOCKET")
    print(context.get("IP"), context.get("PORT"))
    addr = (context.get("IP"), context.get("PORT"))
    sock.bind(addr)
    sock.listen(1)



    while True:
        client_socket, client_address = sock.accept()
        data = client_socket.recv(1024).decode()
        print(f"Received data : {data}")
