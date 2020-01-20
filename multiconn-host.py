#!/usr/bin/env python

import socket
from _thread import *
import threading
import traceback

printLock = threading.Lock()
connections = []


def listenerThread(connData):
    global connections
    global sendQueue

    c, addr = connData

    while True:
        # Receive data
        try:
            data = c.recv(1024)
            if not data:
                raise Exception('crap')
        except:
            print('Bye {}!'.format(addr[0]))
            c.close()
            printLock.acquire()
            connections.remove(connData)
            printLock.release
            break

        # Print message
        print(addr[0], ':', data.decode('utf-8'))

        # Update the data to send
        sendQueue.append(data)

        # Send bulk message to everyone connnected
        printLock.acquire()
        sendData = sendQueue.pop()
        for connection in connections:
            connection[0].send(sendData)
        printLock.release()

def main():
    global connections
    global sendQueue

    host = '130.108.202.158'
    port = 65432

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            print('Socket bound to port', port)
            break
        except:
            print('Failed to start host')
            port += 1
            print('Trying to listen on port {}'.format(port))
    print()

    s.listen(5)

    connections = []
    sendQueue = []

    try:
        while True:
            c, addr = s.accept()

            connData = (c, addr)
            printLock.acquire()
            connections.append(connData)
            printLock.release()

            print('Connections:', end=' ')
            for conn in connections:
                print(conn[1][0], end=' ')
            print()

            start_new_thread(listenerThread, (connData,))
            # c.sendall(b'bugger off')
    except:
        print('Host crashed (fatal error in while loop)')
        s.close()


if __name__ == '__main__':
    main()
