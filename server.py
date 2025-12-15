import socket
import threading
import sqlite3
import hashlib

class Server:
    def __init__(self, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server running on {self.host}:{self.port}")

        self.setup_database()

    def setup_database(self):
        """יוצר את טבלת המשתמשים במסד הנתונים"""
        conn = sqlite3.connect("db_init/users.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def handle_client(self, conn, addr):
        print(f"🟢 New connection from {addr}")
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                command, *params = data.split('|')

                if command == "LOGIN":
                    username, password = params
                    if self.verify_user(username, password):
                        conn.send("LOGIN_SUCCESS".encode())
                    else:
                        conn.send("LOGIN_FAILED".encode())

                elif command == "SIGNUP":
                    username, password = params
                    if self.add_user(username, password):
                        conn.send("SIGNUP_SUCCESS".encode())
                    else:
                        conn.send("SIGNUP_FAILED".encode())

                else:
                    conn.send("UNKNOWN_COMMAND".encode())

            except:
                break

        conn.close()
        print(f"🔴 Connection with {addr} closed")

    def verify_user(self, username, password):
        """בודק אם המשתמש קיים במסד הנתונים"""
        conn = sqlite3.connect("db_init/users.db")
        c = conn.cursor()
        hashed_password = '1'+hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        result = c.fetchone()
        conn.close()
        return result is not None

    def add_user(self, username, password):
        """מוסיף משתמש חדש למסד הנתונים"""
        try:
            conn = sqlite3.connect("db_init/users.db")
            c = conn.cursor()
            hashed_password = '1'+hashlib.sha256(password.encode()).hexdigest()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False

    def run(self):
        print("🖥️ Waiting for connections...")
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    Server().run()
