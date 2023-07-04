import socket
import threading

nickname = input('Choose a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.5.52.23', 5555))

def recieve():
    while True:
        try:
            message = client.recv(1024)
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occured')
            client.close()
            break

def write():
    message = f'{nickname}: (input(" "))'
    client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()