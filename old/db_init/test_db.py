import sqlite3

conn = sqlite3.connect("../../server/db/users.db")
cursor = conn.cursor()

cursor.execute("""
SELECT players.first_name,
       players.last_name,
       players.club
FROM players
JOIN user_players ON players.id = user_players.player_id
JOIN users ON users.id = user_players.user_id
WHERE users.username = 'a';
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
