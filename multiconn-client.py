#!/usr/bin/env python

import socket
from _thread import *
import threading
from sys import argv

def listenerThread(s):
    while True:
        data = s.recv(1024)
        print('HOST:', str(data.decode('ascii')))

def main():
    host = '130.108.202.158'
    port = 65432 if len(argv) < 2 else int(argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    start_new_thread(listenerThread, (s,))

    while True:
        s.send(input('Enter message to send:').encode('ascii'))
    s.close()


if __name__ == '__main__':
    main()
