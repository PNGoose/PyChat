import socket
import time


class Server:
    def __init__(self, ip='localhost', port=9090, name='Server', connects=5):
        self.serv = socket.socket()
        self.ip, self.port = ip, port
        self.name = name
        self.serv.bind((ip, port))
        self.connections, self.users = [], {}
        self.serv.listen(connects)
        print('start')


    def connect_client(self):
        self.serv.setblocking(False)
        con, address = self.serv.accept()
        print('connected:', con)
        newname = con.recv(1024)
        self.connections.append(con)
        self.users[con] = newname
        print('connected:', newname.decode())
        self.serv.send(f'Добро пожаловать на сервер {self.name}!'.encode())
        self.serv.setblocking(True)

    def mainloop(self):
        while True:
            print('...', end='')
            try:
                self.connect_client()
            except: pass
            for i in self.connections:
                try:
                    message = i.recv(1024)
                    for i in self.connections:
                        self.serv.send(self.users[i].encode() + message)
                except: pass

            time.sleep(1)


serve = Server()
serve.mainloop()
