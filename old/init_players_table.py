import sqlite3

# Path to your database file (will be created if not exists)
db_path = "players.db"

# Path to the SQL file you want to run
# sql_file_path = "players.sql"

def run_sql_file(db_path, sql_file_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read SQL script
    with open(sql_file_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("SQL script executed successfully!")

if __name__ == "__main__":
    run_sql_file(db_path, sql_file_path)
