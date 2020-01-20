#!/usr/bin/env python
import socket

HOST = '130.108.202.158'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            toSend = input('Enter message to send: ')
            conn.sendall(toSend.encode('utf-8'))

            data = conn.recv(1024)
            print(addr, ':', data.decode('utf-8'))

        # print('Connected by', addr)
        # while True:
        #     data = conn.recv(1024)
        #     if not data:
        #         break
        #     conn.sendall(data)
