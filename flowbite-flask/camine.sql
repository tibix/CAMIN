-- MariaDB dump 10.19  Distrib 10.9.3-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: camine
-- ------------------------------------------------------
-- Server version	10.9.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `camin`
--

DROP TABLE IF EXISTS `camin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `camin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nume` varchar(255) NOT NULL,
  `adresa` text DEFAULT NULL,
  `site` text DEFAULT NULL,
  `telefon` text NOT NULL,
  `pret` int(11) NOT NULL,
  `note` text DEFAULT NULL,
  `verificat` tinyint(1) NOT NULL,
  `adaugat` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `camin_nume` (`nume`),
  KEY `camin_adresa` (`adresa`(3072)),
  KEY `camin_site` (`site`(3072)),
  KEY `camin_telefon` (`telefon`(3072)),
  KEY `camin_pret` (`pret`),
  KEY `camin_note` (`note`(3072)),
  KEY `camin_verificat` (`verificat`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camin`
--

LOCK TABLES `camin` WRITE;
/*!40000 ALTER TABLE `camin` DISABLE KEYS */;
INSERT INTO `camin` VALUES
(1,'Caminul de Varstnici Mosia Seniorilor','Str. Braniste 119 407310 Comuna Gilau, Cluj','https://www.facebook.com/Mosia-seniorilor-camin-de-batrani-482451695280740/','[\'0744 652 870\']',5500,'4500 (3 in camera) / 5500 (2 in camera). Nu sunt locuri momentan. Sa nu fie bolnav de schizofrenie sau cancer.',1,'2022-09-27'),
(2,'Casa de ingrijire Raisa - Turda','','','[\'0741 080 823\']',0,'',0,'2022-09-27'),
(3,'Caminul Bunici Fericiti','Tauti - Floresti','https://www.facebook.com/caminbunicifericiti/?ref=page_internal','[\'0744182528\']',4000,'Posibil un loc la etaj (camera single); Camera double sau triple - 3500',1,'2022-09-27'),
(4,'Camin Sfantul Sava','Loc Copaceni, jud. Cluj, DN1, KM 453+300m, Cluj Napoca-Turda','https://www.azilcluj.ro/','[\'0757459717\']',0,'',0,'2022-09-27'),
(5,'Asociatia Rebeca','Localitatea Santioana, nr. 304B, comuna Taga','https://caminvarstnicirebeca.ro/','[\'0748 201 020\']',0,'',0,'2022-09-27'),
(6,'Casa Cristiana','Strada Principala nr 77E, Salicea 407236','https://casacristiana.ro/','[\'0744 522 754\']',0,'',0,'2022-09-27'),
(7,'Camin Varstinici Fileo','Luna de Sus','','[\'0751 499 177\', \'0723 282 617\']',0,'',0,'2022-09-27'),
(8,'Maicuta Mera - Fundatia Crestina','Loc. Mera, Nr. 86-87, Baciu, Cluj','','[\'0264281222\', \'0264420170\']',0,'',0,'2022-09-27'),
(9,'Casa Theodora','Str. Timisului, Nr. 12, Cluj-napoca, Cluj','https://www.batranifericiti.ro/companie/Casa-Theodora.html','[\'0264 416 768\', \'0723669135\', \'0720062580\', \'0723526322\', \'0264417656\']',4000,'Nu sunt locuri momentan. Trebuie depusa cerere pentru a fii in baza de date.',1,'2022-09-27'),
(10,'Sara Anastasia','Str. Libertatii Nr. 163, Apahida, Cluj-Napoca','http://www.azilbatranicluj.com (nefunctional)','[\'0747 932 192\']',3500,'Sunt locuri libere',1,'2022-09-27'),
(11,'Casa Betsaida','Salicea nr. 71, jud. Cluj','caminbatranicluj.ro','[\'+40 724 200 413 (L-V: 9-17) - internari/locuri\', \'0747 253 905 (L-V: 9-17) - informatii generale\']',0,'',0,'2022-09-27'),
(12,'Asociatia Capernaum','Str. Principala, Nr. 385 A, Buza, Cluj','http://asociatiacapernaum.com/ (nefunctional)','[\'0745 220 990\']',0,'',0,'2022-09-27'),
(13,'Casa Hermina Gilau','str Braniste, nr. 25A, Gilau','https://casahermina.ro/ro','[\'0749-166 774\']',0,'',0,'2022-09-27'),
(14,'Casa Hermina Dezmir','str. Planoarelor, nr.7, Dezmir','https://casahermina.ro/ro','[\'0749-166 774\']',0,'',0,'2022-09-27'),
(15,'Casa Greta','Strada Ion Ionescu de la Brad 12, Cluj-Napoca 400394, Someseni','https://www.azil-batrani.com/','[\'0740 511 586\']',3500,'Sunt locuri, dar trebuie sa ne miscam repede.',1,'2022-09-27'),
(16,'Valea Izvoarelor','Apahida','https://valeaizvoarelor.com/cluj-senior-village/','[\'+40 722 224 589\']',0,'',0,'2022-09-27');
/*!40000 ALTER TABLE `camin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilizator`
--

DROP TABLE IF EXISTS `utilizator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `utilizator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nume` varchar(255) NOT NULL,
  `adresa` text DEFAULT NULL,
  `telefon` text NOT NULL,
  `note` text DEFAULT NULL,
  `verificat` tinyint(1) NOT NULL,
  `adaugat` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilizator_nume` (`nume`),
  KEY `utilizator_adresa` (`adresa`(3072)),
  KEY `utilizator_telefon` (`telefon`(3072)),
  KEY `utilizator_note` (`note`(3072)),
  KEY `utilizator_verificat` (`verificat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilizator`
--

LOCK TABLES `utilizator` WRITE;
/*!40000 ALTER TABLE `utilizator` DISABLE KEYS */;
/*!40000 ALTER TABLE `utilizator` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-29 18:00:11
