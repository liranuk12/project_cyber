import json
import socket
import struct
from io import BytesIO

from PIL import Image


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

    def get_player_image(self, player_id):
        # בקשה
        msg = f"GET_PLAYER_IMAGE|{player_id}"
        self.client_socket.sendall(msg.encode())

        # קבלת אורך
        raw_len = self.client_socket.recv(4)
        img_len = struct.unpack(">I", raw_len)[0]

        # קבלת התמונה עצמה
        image_bytes = b""
        while len(image_bytes) < img_len:
            chunk = self.client_socket.recv(4096)
            image_bytes += chunk

        # בניית תמונה
        img = Image.open(BytesIO(image_bytes))
        return img

    def buy_player(self, user_id, player_id):
        msg = f"BUY_PLAYER|{user_id}|{player_id}"
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(1024).decode()

    def get_my_team(self, user_id):
        msg = f"MY_TEAM|{user_id}"
        self.client_socket.sendall(msg.encode())

        data = self.client_socket.recv(16384).decode()
        response = json.loads(data)

        if response.get("status") != "OK":
            return []

        return response.get("players", [])

    def close(self):
        self.client_socket.close()