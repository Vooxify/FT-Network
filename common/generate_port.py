import random as r
from common.context import Context

server_port = Context()
base_values = [1024, 65535]
incorrect_port = [49152, 65535]


def is_valid_port(port):
    return base_values[0] <= port <= base_values[1] and port not in incorrect_port


# Check if the port is good
def correct_port(port):
    if is_valid_port(port):
        print("[+]  Successfully checked the custom port.")
        return port

    while True:
        re_type = input(f"[!]  The port is invalid. Choose one between {base_values[0]} and {base_values[1]} : ")
        try:
            re_type = int(re_type)
        except ValueError:
            print("[!] Error in value. ")
            continue

        if is_valid_port(re_type):
            return re_type
        else:
            print("[!] This port is not allowed !")


def generate_custom_port(custom_port):
    if custom_port is None:
        port = r.randint(base_values[0], base_values[1])
        print("[+]  Random port was generated.")
        port = correct_port(port)
        print("[+]  Successfully set the port for the server")
        server_port.set("PORT", port)
    else:
        print("[+]  Checking the port.")
        port = correct_port(custom_port)
        print("[+]  Successfully set the port for the server")
        server_port.set("PORT", port)
