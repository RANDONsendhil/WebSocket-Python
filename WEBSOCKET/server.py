#coding:utf8
import socket
import threading
# From Server Side

class clientThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        data = conn.recv(1024)
        data = data.decode('utf8')
        print(data)


host,port = ('',7000)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))

print("Server started...")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("Listening...")
    my_thread = clientThread(conn)
    my_thread.start()

conn.close()
socket.close()






