
import socket

def resolve(name):
    if name == "mpapp.nobies.in":
        return "172.16.45.84"
    else :
        # you ought to add some basic checking of name here
        return socket.gethostbyname(name)

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        bits = data.split(":")
        if bits[0] == 'h':
            client.send(resolve(bits[1]))
    client.close()
