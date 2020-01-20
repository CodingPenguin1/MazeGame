#!/usr/bin/env python

import socket
from _thread import *
import threading

printLock = threading.Lock()


def listenerThread(c):
    while True:
        # Receive data
        data = c.recv(1024)

        # If can't receive data, kill process
        if not data:
            print('Bye')
            printLock.release()
            break

        # Send data back to client, but reversed
        data = data[::-1]
        c.send(data)
    c.close()


def main():
    host = '130.108.202.158'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('Socket bound to port', port)

    s.listen(5)

    while True:
        c, addr = s.accept()

        printLock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        start_new_thread(listenerThread, (c,))
    s.close()


if __name__ == '__main__':
    main()
