"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import socket

soc: socket.socket = socket.socket()

soc.bind(("127.0.0.1", 9000))
soc.listen()
while True:
    con, addr = soc.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    print(f"Buffer from connection: {con.recv(1024)}")
    con.send(b"Copy that!")
    break
