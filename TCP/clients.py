import socket
import threading
import argparse


parser = argparse.ArgumentParser(description='fetch server host and port')
parser.add_argument('-H', '--host', type=str, required=True, help='Ip address of the server')
parser.add_argument('-p', '--port', type=int, required=True, help='port number of the server ')
args = parser.parse_args()


nickname = input('Choose a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((args.host, args.port))


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