from common.context import Context
from common.get_file_path import get_file_path
from common.get_server_ip_and_port import get_server_ip_and_port
from file_transfer_type.client.start_client import start_client

context = Context()
# Globals methods
socket = context.get("SOCKET")


def run():
    get_server_ip_and_port()
    start_client()

    while True:
        msg = input("data : ")

        socket.sendall(msg.encode())


