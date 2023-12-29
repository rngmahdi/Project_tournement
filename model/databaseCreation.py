from tkinter import *
import connection

connect = connection.Connection()
cursor = connect.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dbtournament")
cursor.execute("use dbtournament")
#! create the tournament table 
cursor.execute("CREATE TABLE IF NOT EXISTS `tournament` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `title` varchar(30) NOT NULL,\
  `place` varchar(50) NOT NULL,\
  `Date` date NOT NULL,\
  `name_of_creator` varchar(30) NOT NULL,\
  `type` varchar(30) NOT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;\
")
#! create the player table
cursor.execute("CREATE TABLE IF NOT EXISTS `player` (\
  `idPlayer` int(11) NOT NULL AUTO_INCREMENT,\
  `fullname` varchar(50) NOT NULL,\
  `rating` int(11) NOT NULL,\
  `phone` varchar(12) NOT NULL,\
  `email` varchar(80) NOT NULL,\
  PRIMARY KEY (`idPlayer`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;")
#! create the match table 
cursor.execute("CREATE TABLE IF NOT EXISTS `matches` (\
  `idmatch` int(11) NOT NULL AUTO_INCREMENT,\
  `idplayer1` int(11) NOT NULL,\
  `resultat1` float NOT NULL,\
  `idplayer2` int(11) NOT NULL,\
  `resultat2` float NOT NULL,\
  `round` varchar(25) NOT NULL,\
  PRIMARY KEY (`idmatch`),\
  KEY `idplayer1` (`idplayer1`),\
  KEY `idplayer2` (`idplayer2`),\
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`idplayer1`) REFERENCES `player` (`idPlayer`),\
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`idplayer2`) REFERENCES `player` (`idPlayer`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;\
")

