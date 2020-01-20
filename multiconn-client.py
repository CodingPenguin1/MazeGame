#!/usr/bin/env python

import socket


def main():
    host = '130.108.202.158'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = 'message from client'
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('Received:', str(data.decode('ascii')))
        if input('\nDo you want to continue(y/n) :') == 'y':
            continue
        else:
            break
    s.close()


if __name__ == '__main__':
    main()
