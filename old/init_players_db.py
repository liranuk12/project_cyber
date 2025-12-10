
# run_script.py
import subprocess

# הרצת הסקריפט
subprocess.run(["python", "C:/Users/liranuk/Documents/project_cyber/verify_images_and_build_sql.py"])


# import sqlite3
#
# # 1. Define the data for the player
# # NOTE: The values for 'club_logo' and 'photo' are placeholder URLs.
# # You will need to replace these with actual Wikimedia links.
# player_data = (
#     1,  # id
#     "Lionel",  # first_name
#     "Messi",  # last_name
#     "Argentina",  # country
#     "Forward",  # position
#     "Inter Miami CF",  # club
#     "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Inter_Miami_CF_logo.svg/120px-Inter_Miami_CF_logo.svg.png",
#     # club_logo (Placeholder)
#     "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel_Messi_Copa_Am%C3%A9rica_2021_%28cropped%29.jpg",
#     # photo (Placeholder)
#     95,  # attack (TINYINT max is 255, 95 is fine)
#     40,  # defense
#     98  # possession
# )
#
# # 2. Define the SQL INSERT statement
# sql_insert = """
# INSERT INTO players (
#     id, first_name, last_name, country, position,
#     club, club_logo, photo, attack, defense, possession
# )
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """
#
# # 3. Connect to the database and execute the query
# conn = None
# try:
#     # Connect to your database file (e.g., 'players.db')
#     # If the file doesn't exist, SQLite will create it.
#     conn = sqlite3.connect('players.db')
#     cursor = conn.cursor()
#
#     # Execute the insert statement with the player_data
#     cursor.execute(sql_insert, player_data)
#
#     # Commit the transaction to save the changes to the database
#     conn.commit()
#     print("✅ Successfully inserted player data!")
#
# except sqlite3.Error as e:
#     print(f"❌ Database error occurred: {e}")
# finally:
#     # Close the connection
#     if conn:
#         conn.close()