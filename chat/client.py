import socket
import argparse
import sys
import threading
import select

parser = argparse.ArgumentParser()
parser.add_argument("ip_address")
parser.add_argument("port", type=int)
parser.add_argument("username", type=str)
args = parser.parse_args()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = args.ip_address
port = args.port

server.connect((ip_address, port))
server.send(args.username.encode())

lsock, rsock = socket.socketpair()

def readFromUser(sock):
    while True:
        userinput = input()
        sock.send(str.encode(userinput))

x = threading.Thread(target=readFromUser, args=(rsock, ))
x.start()

while True:
    sockets_list = [lsock, server]
    read_socket, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_socket:
        if socks == server:
            message = socks.recv(2048)
            message = message.decode("utf-8")
            if len(message) > 0:
                print(message)
        else:
            message = socks.recv(2048)
            server.send(message)
            print("<You> " + message.decode('utf-8'))

server.close()
