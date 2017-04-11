import socket

### configure me ###

dns_server_ip = '127.0.0.1'
dns_server_port = 50000
query = 'mpapp.nobies.in' # change this to the hostname you want to lookup

### configure me ###

size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dns_server_ip,dns_server_port))
s.send('h:' + query)
data = s.recv(size)
s.close()
print data
