import threading
import socket

host = '0.0.0.0'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            client.remove(client)
            nickname = nickname(index)
            broadcast(f"{nickname} left the chat ".encode(  ascii-8))
            nickname.remove(nickname)
            break
def recieve():
    while True:
        client, address = server.accept()
        print(F"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients .append(client)


        print(f"nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send("connected to the server".encode('ascii'))

        thread = threading.Thread(target = handle, args =(client,))
        thread.start()

print('server is listening...')
recieve()






