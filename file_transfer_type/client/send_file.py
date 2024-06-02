from common.context import Context
from common.get_server_ip_and_port import get_server_ip_and_port


context = Context()
# Globals methods
socket = context.get("SOCKET")


def run():
    get_server_ip_and_port()
    socket.connect((context.get("SERVER_IP"), context.get("SERVER_PORT")))

    while True:
        msg = input("data : ")
        socket.sendall(msg.encode())

        if msg.lower() == "quit":
            break
    socket.close()