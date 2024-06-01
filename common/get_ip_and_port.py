from common.context import Context
import requests

server_port = Context()


def get_ip_and_port():
    print("[+]  Searching public IP.")
    response = requests.get('https://api.ipify.org')

    if response.status_code == 200:
        print("[+]  Successfully found public IP.")
        server_port.set("IP", response.text)
    else:
        raise Exception('Failed to get public IP')
