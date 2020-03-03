import socket
import argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument("ip_address")
parser.add_argument("port", type=int)
args = parser.parse_args()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = args.ip_address
port = args.port

server.bind((IP_address, port))

server.listen(5)

list_connections = list()
list_usernames = list()

def broadcastDisconnect(connection, username):
    for client in list_connections:
        client.send(str.encode("{0} has disconnect.".format(username)))


def clientthread(connection, address, username):
    connection.send("Welcome to my chat room.".encode())

    while True:
        try:
            message = connection.recv(2048)
        except ConnectionResetError:
            remove(connection)
            broadcastDisconnect(connection, username)
            return
        print("Message length: " + str(len(message)))
        if message:
            print("<" + username + "> " + message.decode("utf-8"))
            message_to_send = "<" + username + "> " + message.decode("utf-8")
            broadcast(message_to_send.encode(), connection, username)
        else:
            remove(connection)

def broadcast(message, connection, username):
    for client, user in zip(list_connections, list_usernames):
        if user != username:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection in list_connections:
        list_connections.remove(connection)

while True:
    connection, address = server.accept()
    username = connection.recv(2048)
    username = username.decode("utf-8")
    list_usernames.append(username)

    list_connections.append(connection)

    print(username + " connected")
    x = threading.Thread(target=clientthread,args=(connection, address, username))
    x.start()

connection.close()
server.close()