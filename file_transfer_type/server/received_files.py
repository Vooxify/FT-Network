from common.context import Context

context = Context()

socket = context.get("SOCKET")

def receive_data(connect, client_address):
    # FOR DEV :
    context.set("IP", "localhost")

    try:
        print(f"[+]  Established connection with {client_address}")
        data = connect.recv(1024)
        print(f"[+]  Data received from {client_address} : {data.decode()}")

    finally:
        print("[!]  Connection ERROR !")
        connect.close()
