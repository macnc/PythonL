#!/usr/local/bin/python3
# _*_coding: utf-8

# Code to execute in an independent thread


import time
from threading import Thread
from socket import socket

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

if t.is_alive():
    print('Still running!')
else:
    print('Completed!')

# class IOTask:
#     def terminate(self):
#         self._running = False
#
#     def run(self, sock):
#         # Sock is a socket
#         sock.settimeout(5)
#         while self._running:
#             # Perform a blocking I/O operation w/ timeout
#             try:
#                 data = sock.recv(8172)
#                 break
#             except socket.timeout:
#                 # Continued processing
#                 continue
#
#         # Terminated
#         return
#
#
# class CountdownTask():
#     def __init__(self):
#         self.running = True
#
#     def terminate(self):
#         self.running = False
#
#     def run(self, n):
#         while self.running and n > 0:
#             print('T-minus', n)
#             n -= 1
#             time.sleep(1)
#
# c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
#
# c.terminate()
# t.join()