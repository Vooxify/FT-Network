from common.context import Context
import socket, time

context = Context()

# Globals methods

context.set("SOCKET", socket.socket(socket.AF_INET, socket.SOCK_STREAM))

def check_ip_and_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            return True
        except socket.timeout:
            pass
        except OSError:
            pass
    return False


def test_server(host, port):
    return True if check_ip_and_port(host=host, port=port) else False


def get_server_ip_and_port():
    raw_ip = input("[?]  Please enter the server IP : ")
    raw_port = input("[?]  Please enter the port of the the server : ")

    while True:

        try:
            raw_port = int(raw_port)
            # This 2 lines is for test !
            # To use this code, place them under the print method under if at the end
            context.set("SERVER_IP", raw_ip)
            context.set("SERVER_PORT", raw_port)

            break
        except ValueError:
            raw_port = input("[!]  Please enter a number : ")
            continue

    if test_server(host=raw_ip, port=raw_port):
        print("[+]  The server was online !")
    else:
        print("[!]  The server is inacessible, check the IP/port and check if the server port is opened !")
