from common.context import Context
import socket as s

context = Context()


def start_server():
    context.set("IP", "localhost")
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    address = (context.get("IP"), context.get("PORT"))
    print(address)
    socket.bind(address)

    socket.listen(1)

    print("[+]  Started connection.")
    connection, client_adress = socket.accept()
    print(f"[+]  New connection was detected ! {client_adress}")

    connection.close()
