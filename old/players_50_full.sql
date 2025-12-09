DROP TABLE IF EXISTS players;

CREATE TABLE players (
  id INT PRIMARY KEY,
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

INSERT INTO players (id, first_name, last_name, country, position, club, club_logo, photo, attack, defense, possession) VALUES
(1, 'Lionel', 'Messi', 'Argentina', 'Forward', 'Inter Miami', 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Inter_Miami_CF_logo.svg/1200px-Inter_Miami_CF_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/8/89/Lionel_Messi_20180626.jpg', 95, 38, 91),
(2, 'Cristiano', 'Ronaldo', 'Portugal', 'Forward', 'Al Nassr', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Al_Nassr_FC_logo.svg/1200px-Al_Nassr_FC_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg', 94, 35, 88),
(3, 'Kylian', 'Mbappé', 'France', 'Forward', 'Paris Saint-Germain', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/1200px-Paris_Saint-Germain_F.C..svg.png', 'https://upload.wikimedia.org/wikipedia/commons/a/a8/Kylian_Mbappe_2022.jpg', 92, 36, 89),
(4, 'Kevin', 'De Bruyne', 'Belgium', 'Midfielder', 'Manchester City', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Kevin_De_Bruyne_20180709.jpg', 88, 70, 94),
(5, 'Virgil', 'van Dijk', 'Netherlands', 'Defender', 'Liverpool', 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC_logo.svg/1200px-Liverpool_FC_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/2/25/Virgil_van_Dijk_2018.jpg', 65, 92, 80),
-- הוסף כאן עוד שחקנים עד 50
(6, 'Erling', 'Haaland', 'Norway', 'Forward', 'Manchester City', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Erling_Haaland_2022.jpg', 93, 38, 85),
(7, 'Mohamed', 'Salah', 'Egypt', 'Forward', 'Liverpool', 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC_logo.svg/1200px-Liverpool_FC_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/9/97/Mohamed_Salah_2018.jpg', 91, 40, 87),
(8, 'Sadio', 'Mané', 'Senegal', 'Forward', 'Al Nassr', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Al_Nassr_FC_logo.svg/1200px-Al_Nassr_FC_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Sadio_Mane_2022.jpg', 90, 42, 86),
(9, 'Robert', 'Lewandowski', 'Poland', 'Forward', 'Barcelona', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/1200px-FC_Barcelona_%28crest%29.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Robert_Lewandowski_2022.jpg', 92, 38, 85),
(10, 'Neymar', 'Jr', 'Brazil', 'Forward', 'Al-Hilal', 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Al-Hilal_FC_logo.svg/1200px-Al-Hilal_FC_logo.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/8/87/Neymar_2018.jpg', 91, 36, 88);
