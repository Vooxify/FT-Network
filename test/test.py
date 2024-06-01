import socket as s

from common.context import Context

context = Context()

socket = s.socket(s.AF_INET, s.SOCK_STREAM)

address = (context.get("IP"), context.get("PORT"))

socket.connect(address)
