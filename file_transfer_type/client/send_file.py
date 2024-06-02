from common.context import Context
from common.get_server_ip_and_port import get_server_ip_and_port


context = Context()
# Globals methods
socket = context.get("SOCKET")

def connect_server():
    socket.connect((context.get("SERVER_IP"), context.get("SERVER_PORT")))


def run():
    get_server_ip_and_port()
    connect_server()

