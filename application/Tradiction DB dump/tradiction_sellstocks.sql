CREATE DATABASE  IF NOT EXISTS `tradiction` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `tradiction`;
-- MySQL dump 10.13  Distrib 8.0.17, for macos10.14 (x86_64)
--
-- Host: localhost    Database: tradiction
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sellstocks`
--

DROP TABLE IF EXISTS `sellstocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sellstocks` (
  `ssid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `sellingprice` varchar(45) NOT NULL,
  `sellingdate` varchar(45) NOT NULL,
  `sellquantity` int(11) NOT NULL,
  `profitloss` varchar(45) NOT NULL,
  `bid` int(11) NOT NULL,
  PRIMARY KEY (`ssid`),
  KEY `lid_idx` (`lid`),
  KEY `buyid_idx` (`bid`),
  CONSTRAINT `buyid` FOREIGN KEY (`bid`) REFERENCES `buystocks` (`bid`),
  CONSTRAINT `logiid` FOREIGN KEY (`lid`) REFERENCES `login` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellstocks`
--

LOCK TABLES `sellstocks` WRITE;
/*!40000 ALTER TABLE `sellstocks` DISABLE KEYS */;
INSERT INTO `sellstocks` VALUES (4,32,'148.21','Thu May 21 20:47:12 2020',100,'0',8),(5,32,'148.21','Thu May 21 23:12:55 2020',10,'0',10),(6,32,'32.23','Thu May 21 23:55:45 2020',10,'0',11),(7,32,'32.23','Fri May 22 01:00:11 2020',10,'0',11),(8,32,'30.26','Fri May 22 01:40:33 2020',10,'0',13),(9,32,'30.26','Fri May 22 02:13:34 2020',20,'0',14);
/*!40000 ALTER TABLE `sellstocks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-24 14:39:01
