# import file_transfer_type.server.recived_files as server
from file_transfer_type.server.start_server import start_server

error = [
    "\n\n",
    "CTRL + C was pressed, stop the program",
    "CTRL + C was pressed, stop the program",
    "CTRL + C was pressed, stop the program",
    "\n\n",
]

try:
    print("To call server on windows / linux, install ncat and type 'nc -vz <ip> <port>'")
    q = input("s or c ? ")

    if q == "s":
        start_server()
        pass



except KeyboardInterrupt:
    for i in error:
        print(i)
