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
        if msg != "file":
            socket.sendall(msg.encode())
        if msg.lower() == "file":
            get_file_path()
            socket.sendall(context.get("FILE_PATH").encode())

            with open(context.get("FILE_PATH").split("/")[-1].encode(), "rb") as file:
                # Do a progress bar here
                data = file.read()
                if not data:
                    break
                socket.sendall(data)

        elif msg.lower() == "quit":
            break
    socket.close()

