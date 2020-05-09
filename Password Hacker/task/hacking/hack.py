# write your code here
import itertools
import socket
import sys


def password_generator(length):
    for m in itertools.product(itertools.chain(range(97, 123), range(48, 58)), repeat=length):
        yield ''.join(map(chr, iter(m)))


args = sys.argv
ip = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (ip, port)
    client_socket.connect(address)
    message = 'Wrong password!'
    password = ""

    i = 1

    while message == 'Wrong password!':
        for p in password_generator(i):
            client_socket.send(p.encode())
            response = client_socket.recv(1024)
            message = response.decode()
            if message != 'Wrong password!':
                password = p
                break
        i += 1

    if message == 'Connection success!':
        print(password)
    else:
        print("Too Many attempts")

