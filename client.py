#!/usr/bin/env python

import socket

HOST = '130.108.202.158'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        toSend = input('Enter message to send: ')
        s.sendall(toSend.encode('utf-8'))

        data = s.recv(1024)
        print('HOST:', data.decode('utf-8'))
