import socket

class Client:
    def __init__(self, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def login(self, username, password):
        msg = f"LOGIN|{username}|{password}"
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(1024).decode()

    def signup(self, username, password):
        msg = f"SIGNUP|{username}|{password}"
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(1024).decode()
