DROP TABLE IF EXISTS players;

CREATE TABLE players (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
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

-- INSERTS (id as NULL for autoincrement)
INSERT INTO players VALUES (NULL,'Jordi','Alba','ESP','LB','Inter Miami','miami.png','alba.jpg',70,72,78);
--INSERT INTO players VALUES ('Cristiano','Ronaldo','PRT','ST','Al Nassr','alNassr.png','alNassr.png','ronaldo.jpg',94,40,72);
--INSERT INTO players VALUES ('Ronald','Araújo','URU','CB','Barcelona','barca.png','araujo.jpg',70,88,62);
--INSERT INTO players VALUES ('Gabriel','Magalhães','BRA','CB','Arsenal','arsenal.png','arsenal.png','arsenal.png'); -- placeholder in case you want
--INSERT INTO players VALUES ('Ansu','Fati','ESP','LW','Barcelona','barca.png','barca.png','barca.png');
---- (note: above three lines were placeholders if you want; keep or remove)
--
---- Accurate entries derived from your file list:
--INSERT INTO players VALUES ('Ronald','Araújo','URU','CB','Barcelona','barca.png','araujo.jpg',68,89,57);
--INSERT INTO players VALUES ('Jorge','(Arsenal logo)','ENG','?','Arsenal','arsenal.png','arsenal.png',50,50,50);
--
---- Real entries (from your file list) — main block:
--INSERT INTO players VALUES ('Jordi','Alba','ESP','LB','Inter Miami','miami.png','alba.jpg',69,74,80);
--INSERT INTO players VALUES ('Cristiano','Ronaldo','PRT','ST','Al Nassr','alNassr.png','ronaldo.jpg',95,39,71);
--INSERT INTO players VALUES ('Ronald','Araújo','URU','CB','Barcelona','barca.png','araujo.jpg',67,88,60);
--INSERT INTO players VALUES ('Unknown','ArsenalLogo','ENG','?','Arsenal','arsenal.png','arsenal.png',50,50,50);
--INSERT INTO players VALUES ('Unknown','BarcaLogo','ESP','?','Barcelona','barca.png','barca.png',50,50,50);
--INSERT INTO players VALUES ('Unknown','BayernLogo','DEU','?','Bayern Munich','bayern.png','bayern.png',50,50,50);
--
---- PLEASE IGNORE the three "Unknown" placeholder lines above if you don't need them.
---- Now the rest of the players from your list (generated with best-known club in 2025 and logos only when available):
--
--INSERT INTO players VALUES ('Jude','Bellingham','ENG','CM','Real Madrid','real_madrid.png','bellingham.jpg',90,65,86);
--INSERT INTO players VALUES ('Sergio','Busquets','ESP','CDM','Inter Miami','miami.png','busquets.jpg',60,68,84);
--INSERT INTO players VALUES ('Thibaut','Courtois','BEL','GK','Real Madrid','real_madrid.png','courtois.jpg',25,90,30);
--INSERT INTO players VALUES ('Frenkie','de Jong','NED','CM','Barcelona','barca.png','deJong.jpg',78,66,86);
--INSERT INTO players VALUES ('Ousmane','Dembélé','FRA','RW','Paris Saint-Germain','psg.png','dembele.jpg',86,40,78);
--INSERT INTO players VALUES ('Raphinha','Raphinha','BRA','RW','Barcelona','barca.png','raphinha.jpg',85,46,76);
--INSERT INTO players VALUES ('Luis','Díaz','COL','LW','Liverpool','liverpool.png','diaz.jpg',84,52,75);
--INSERT INTO players VALUES ('Xavi','Doué','???','CM','doue.jpg',62,60,68); -- ambiguous player (club NULL)
--INSERT INTO players VALUES ('Fermin','Fermín','???','FW','fermin.jpg',68,35,60); -- ambiguous
--INSERT INTO players VALUES ('Jeremie','Frimpong','NED','RB','Bayer Leverkusen','frimpong.jpg',83,67,74);
--INSERT INTO players VALUES ('Pablo','Gavi','ESP','CM','Barcelona','barca.png','gavi.jpg',80,48,82);
--INSERT INTO players VALUES ('Serge','Gnabry','GER','RW','Bayern Munich','bayern.png','gnabry.jpg',84,58,73);
--INSERT INTO players VALUES ('Leon','Goretzka','GER','CM','Bayern Munich','bayern.png','goretzka.jpg',78,78,72);
--INSERT INTO players VALUES ('Ryan','Gravenberch','NED','CM','Bayern Munich','bayern.png','gravenberch.jpg',77,65,78);
--INSERT INTO players VALUES ('Arda','Güler','TUR','AM','Real Madrid','real_madrid.png','guler.jpg',76,40,77);
--INSERT INTO players VALUES ('Arthur','Gyökeres','SWE','ST','gyokares.jpg',82,42,66);
--INSERT INTO players VALUES ('Erling','Haaland','NOR','ST','Manchester City','haland.jpg',96,40,68);
--INSERT INTO players VALUES ('Harry','Kane','ENG','ST','Bayern Munich','bayern.png','kane.jpg',93,48,70);
--INSERT INTO players VALUES ('Joshua','Kimmich','GER','CDM','Bayern Munich','bayern.png','kimmich.jpg',78,86,82);
--INSERT INTO players VALUES ('Jules','Koundé','FRA','CB','Barcelona','barca.png','kounde.jpg',65,84,68);
--INSERT INTO players VALUES ('Khvicha','Kvaratskhelia','GEO','LW','Napoli','kvara.jpg',89,40,76);
--INSERT INTO players VALUES ('Robert','Lewandowski','POL','ST','Barcelona','barca.png','lewandowski.jpg',92,44,72);
--INSERT INTO players VALUES ('Darwin','Núñez','URU','ST','Liverpool','liverpool.png','liverpool.png','liverpool.png'); -- placeholder if needed
--INSERT INTO players VALUES ('Alexis','Mac Allister','ARG','CM','Liverpool','liverpool.png','macAllister.jpg',78,64,85);
--INSERT INTO players VALUES ('Giorgi','Mamardashvili','GEO','GK','Valencia','mamardashvili.jpg',25,70,35);
--INSERT INTO players VALUES ('Sadio','Mané','SEN','LW','Al Nassr','alNassr.png','mane.jpg',88,45,73);
--INSERT INTO players VALUES ('Marquinhos','Marquinhos','BRA','CB','Paris Saint-Germain','psg.png','marquinhos.jpg',72,90,70);
--INSERT INTO players VALUES ('Gabriel','Martinelli','BRA','LW','Arsenal','arsenal.png','martinelli.jpg',87,44,74);
--INSERT INTO players VALUES ('Enzo','Fernández','ARG','CM','Benfica/PSG? (ambiguous)','martines.jpg',75,62,78); -- 'martines' ambiguous filename
--INSERT INTO players VALUES ('Kylian','Mbappé','FRA','ST','Real Madrid','real_madrid.png','mbappe.jpg',95,46,85);
--INSERT INTO players VALUES ('Rúben','Mendes','POR','LB','Paris Saint-Germain','psg.png','mendes.jpg',72,75,74);
--INSERT INTO players VALUES ('Lionel','Messi','ARG','RW','Inter Miami','miami.png','messi.jpg',94,58,90);
--INSERT INTO players VALUES ('Manuel','Neuer','GER','GK','Bayern Munich','bayern.png','neuer.jpg',20,90,30);
--INSERT INTO players VALUES ('Martin','Ødegaard','NOR','AM','Arsenal','arsenal.png','odegaard.jpg',82,45,88);
--INSERT INTO players VALUES ('Michael','Olise','FRA','RW','olise.jpg',80,45,78);
--INSERT INTO players VALUES ('Raphinha','(duplicate)','BRA','RW','Barcelona','barca.png','raphinha.jpg',85,46,76);
--INSERT INTO players VALUES ('Marcus','Rashford','ENG','LW','Manchester United','rashford.jpg',86,46,77);
--INSERT INTO players VALUES ('David','Raya','ESP','GK','Arsenal','arsenal.png','raya.jpg',24,72,40);
--INSERT INTO players VALUES ('Declan','Rice','ENG','CDM','Arsenal','arsenal.png','rice.jpg',75,85,80);
--INSERT INTO players VALUES ('Cristiano','Ronaldo','PRT','ST','Al Nassr','alNassr.png','ronaldo.jpg',95,39,71);
--INSERT INTO players VALUES ('Bukayo','Saka','ENG','RW','Arsenal','arsenal.png','saka.jpg',88,46,80);
--INSERT INTO players VALUES ('Mohamed','Salah','EGY','RW','Liverpool','liverpool.png','salah.jpg',92,45,79);
--INSERT INTO players VALUES ('William','Saliba','FRA','CB','Arsenal','arsenal.png','saliba.jpg',60,88,64);
--INSERT INTO players VALUES ('Luis','Suárez','URY','ST','suarez.jpg',80,42,68);
--INSERT INTO players VALUES ('Federico','Valverde','URY','CM','Real Madrid','real_madrid.png','valverde.jpg',84,78,83);
--INSERT INTO players VALUES ('Virgil','van Dijk','NED','CB','Liverpool','liverpool.png','vanDijk.jpg',60,92,66);
--INSERT INTO players VALUES ('Vitinha','Vitinha','PRT','CM','Paris Saint-Germain','psg.png','vitinha.jpg',78,56,80);
--INSERT INTO players VALUES ('Yamal','Yamal','ESP','AM','yamal.jpg',75,45,78);
