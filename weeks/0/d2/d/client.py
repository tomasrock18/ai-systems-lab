"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import socket

soc: socket.socket = socket.socket()

soc.connect(("127.0.0.1", 9000))
soc.send(b"Clone wars!")
print(f"Response from server: {soc.recv(1024)}")
