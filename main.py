import file_transfer_type.server.recivedFiles as server

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
        server.main()



except KeyboardInterrupt:
    for i in error:
        print(i)
