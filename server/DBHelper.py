# קובץ זה מכיל פעולות סטטיות בהן השרת משתמש לשלוף או לעדכן מידע מה-DB

DB_PATH = "db/users.db"

import sqlite3
import hashlib

class DBHelper:

    @staticmethod
    def setup_database():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def _hash_password(password: str) -> str:
        return '1' + hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_user(username: str, password: str) -> bool:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        hashed_password = DBHelper._hash_password(password)
        c.execute(
            "SELECT 1 FROM users WHERE username=? AND password=?",
            (username, hashed_password)
        )

        result = c.fetchone()
        conn.close()
        return result is not None

    @staticmethod
    def add_user(username: str, password: str) -> bool:
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()

            hashed_password = DBHelper._hash_password(password)
            c.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()
            return True

        except sqlite3.IntegrityError:
            return False

    @staticmethod
    def load_missing_players(user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, first_name, last_name, position, club
            FROM players
            WHERE id NOT IN (
                SELECT player_id
                FROM user_players
                WHERE user_id = ?
            )
        """, (user_id,))

        rows = cursor.fetchall()
        conn.close()

        players_json = []
        for row in rows:
            players_json.append({
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "position": row[3],
                "club": row[4]
            })

        return players_json

    @staticmethod
    def buy_player(user_id, player_id) -> bool:
        """
        Inserts (user_id, player_id) into user_players table
        Returns True if success, False if already owned or error
        """
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            cursor.execute("""
                   INSERT INTO user_players (user_id, player_id)
                   VALUES (?, ?)
               """, (user_id, player_id))

            conn.commit()
            conn.close()
            return True

        except sqlite3.IntegrityError:
            # שגיאה אם המשתמש כבר קנה את השחקן - לא אמור לקרות כי בחלון הוא בחר מרשימה של שחקנים שאין לו
            return False

        except Exception as e:
            print("DB buy_player error:", e)
            return False

    @staticmethod
    def get_user_team(user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.id, p.first_name, p.last_name, p.position, p.club
            FROM players p
            JOIN user_players up ON p.id = up.player_id
            WHERE up.user_id = ?
        """, (user_id,))

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "first_name": r[1],
                "last_name": r[2],
                "position": r[3],
                "club": r[4]
            }
            for r in rows
        ]

    @staticmethod
    def get_player_image_name(player_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT photo FROM players WHERE id = ?",
            (player_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row and row[0]:
            return row[0]

        return "default.jpg"
