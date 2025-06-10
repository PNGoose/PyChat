import socket
import time

class Client:
    def __init__(self, name='User'):
        self.cli = socket.socket()
        self.name = name
        #self.cli.setblocking(False)

    def connect_server(self, ip='localhost', port=9090):
        try:
            self.cli.connect((ip, port))
            self.cli.recv(1024)
            self.cli.send(self.name.encode())
            greetings = self.cli.recv(1024)
            print(greetings.decode())
        except: pass

    def message(self, text):
        self.cli.send(text.encode())
        self.cli.recv(1024)


clie = Client()
clie.connect_server()
clie.message(input('Input your message: ')))
