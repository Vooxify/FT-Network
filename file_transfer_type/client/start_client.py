from common.context import Context

context = Context()

# Globals methods
socket = context.get("SOCKET")

def start_client():
    try:
        socket.connect((context.get("SERVER_IP"), context.get("SERVER_PORT")))
    except ConnectionRefusedError:
        print("[!]  Server didn't respond.")
        return
