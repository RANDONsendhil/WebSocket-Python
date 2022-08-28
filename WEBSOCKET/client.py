#coding:utf-8
# Added to git
# This is for pull request
# Second pull request from dev to master
import socket
host, port =('localhost',7000)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Client connected...")
    data = "Salut, Coucou, hai..."
    data = data.encode('utf-8')
    socket.sendall(data)
except:
    print("Connection refused")
finally:
    socket.close()

