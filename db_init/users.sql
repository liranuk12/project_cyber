ALTER TABLE users
ADD FOREIGN KEY (players) REFERENCES players(id);