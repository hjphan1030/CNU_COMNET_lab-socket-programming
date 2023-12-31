#!/usr/bin/env python3
# test5
import socket
import time

IP_ADDR = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse tcp port
s.bind((IP_ADDR, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Client address:', addr)
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    currentTime = " " + " new server15 !!! " + time.ctime(time.time()) + "\r\n"
    print(data.decode('utf-8'))
    data = data + currentTime.encode('ascii')
    conn.send(data)  # echo
    conn.close()