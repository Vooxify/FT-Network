from common.get_ip_and_port import get_ip_and_port
from common.context import Context
from common.generate_port import generate_custom_port

from file_transfer_type.server.start_server import start_server

server_port = Context()


def is_integer(msg):
    try:
        int(msg)
        return True
    except ValueError:
        return False


def main():
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
    #    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    get_ip_and_port()
    start_server()


