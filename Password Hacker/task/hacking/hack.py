# write your code here
import socket
import sys

args = sys.argv
ip = args[1]
port = int(args[2])
message = args[3]

client_socket = socket.socket()
address = (ip, port)
client_socket.connect(address)
client_socket.send(message.encode())

response = client_socket.recv(1024)
print(response.decode())

client_socket.close()
