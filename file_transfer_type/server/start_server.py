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
    while True:
        # Acceptez une connexion entrante et créez un nouveau socket pour communiquer avec le client
        connection, client_address = socket.accept()
        try:
            while True:
                # Lisez les données reçues jusqu'à ce que vous détectiez la fin du message
                data = b''
                while not data.endswith(b'\n'):
                    data += connection.recv(1024)

                # Traitez le message reçu
                print('Reçu :', data.decode().strip())

                # Vérifiez si l'utilisateur veut arrêter la communication
                if data.lower() == b'quit\n':
                    break
        finally:
            # Fermez le socket de communication
            connection.close()
