import socket
from test_comm_move import *
import driveboard, time
import sys

# build up connection
driveboard.connect()

PORT = 65434

# create TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
# ip_address = socket.gethostbyname(local_hostname)

# use ethernet address for connection
ip_address = "192.168.1.49"
# ip_address = "127.0.0.1"

# output hostname, domain name and IP address
print("working on {} ({}) with {}".format(local_hostname, local_fqdn, ip_address))

# bind the socket to the port 65431
server_address = (ip_address, PORT)
print("starting up on {} port {}".format(server_address[0], server_address[1]))
s.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
s.listen(1)

driveboard.intensity(0.0)
driveboard.air_on()

# wait for a connection
print("waiting for a connection")
connection, client_address = s.accept()
print(client_address)

try:
    # show who connected to us
    print("connection from {}".format(client_address))

    # receive the data in small chunks and print it
    while True:
        data = connection.recv(1024)
        if data:
            # output received data
            translation = data.decode("utf-8")
            translation = eval(translation)
            # move(translation)
            print(translation)
            control_move(translation)
            # decision = data.decode("utf-8")
            # print(decision)
        else:
            # no more data --quit the loop
            print("no more data")
            break
finally:
    # clean up the connection
    connection.close()

driveboard.close()
