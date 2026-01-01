import json
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

    def get_missing_players(self, user_id):
        """
        Sends MARKET command to server and returns missing players as list of dicts
        """
        try:
            msg = f"MARKET|{user_id}"
            self.client_socket.sendall(msg.encode())

            data = self.client_socket.recv(16384).decode()
            # convert the binary text to object json
            response = json.loads(data)

            if response.get("status") != "OK":
                return []

            return response.get("players", [])

        except Exception as e:
            print("❌ Client error:", e)
            return []

    def buy_player(self, user_id, player_id):
        msg = f"BUY_PLAYER|{user_id}|{player_id}"
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(1024).decode()

    def close(self):
        self.client_socket.close()