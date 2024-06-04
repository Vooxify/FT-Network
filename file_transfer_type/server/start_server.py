import threading
from common.context import Context

context = Context()


# Global

def start_server():

    # FOR DEV REMOVE IF YOU USE !!
    context.set("IP", "localhost")
