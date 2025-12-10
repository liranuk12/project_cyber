import sqlite3

# Path to your SQLite database file
DB_PATH = "players.db"

# The SQL script you provided
SQL_SCRIPT = """
DROP TABLE IF EXISTS players;

CREATE TABLE players (
  id INTEGER PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  country VARCHAR(100),
  position VARCHAR(20),
  club VARCHAR(100),
  club_logo TEXT,
  photo TEXT,
  attack TINYINT,
  defense TINYINT,
  possession TINYINT
);
"""

def setup_database():
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Execute the SQL script
    cursor.executescript(SQL_SCRIPT)

    conn.commit()
    conn.close()
    print("Database initialized and 'players' table created successfully.")

if __name__ == "__main__":
    setup_database()
