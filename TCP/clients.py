import socket
import threading

nickname = input('Choose a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.18.120', 5555))

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

def send_msg():
    while True:
        try:
            message = input('> ')
            client.send(message.encode('ascii'))
        except:
            print('An error occured sending the message')
            client.close()
            break


def write():
    message = f'{nickname}: (input(" "))'
    client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

send_thread = threading.Thread(target=send_msg)
send_thread.start()