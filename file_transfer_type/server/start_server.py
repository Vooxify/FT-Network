import socket
from common.context import Context
from common.generate_port import generate_custom_port
from common.get_ip_and_port import get_ip_and_port
from file_transfer_type.server.received_files import receive_data

context = Context()


# Global

def start_server():

    # FOR DEV REMOVE IF YOU USE !!
    context.set("IP", "localhost")
    is_custom_port = input(
        "[*]  The server listen to a random port who is printed after\n"
        "you want to keep it (more safe) or enter a custom port (less on),\n"
        "type the port number if you want it, else "
        "press 'enter' key "
    )

    # Faire un try pour mettre la valeur en entier
    while True:
        try:
            is_custom_port = int(is_custom_port)
            generate_custom_port(is_custom_port)
            break
        except Exception:
            print("[+]  No port was given, generation started.")

        if is_custom_port == "":
            generate_custom_port(None)
            break
    context.set("SOCKET", socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((context.get("IP"), context.get("PORT")))

    sock.listen(5)
    print("[+]  Waiting for connection.")
    get_ip_and_port()


    c, client_adress = sock.accept()

    receive_data(c, client_adress)
