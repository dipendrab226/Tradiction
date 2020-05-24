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
-- Table structure for table `buystocks`
--

DROP TABLE IF EXISTS `buystocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buystocks` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `stid` int(11) NOT NULL,
  `sname` varchar(45) NOT NULL,
  `datetime` varchar(45) NOT NULL,
  `buyprice` varchar(45) NOT NULL,
  `quantity` varchar(45) NOT NULL,
  `total` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`bid`),
  KEY `stid_idx` (`stid`),
  KEY `lid_idx` (`lid`),
  CONSTRAINT `loginid` FOREIGN KEY (`lid`) REFERENCES `login` (`lid`),
  CONSTRAINT `stid` FOREIGN KEY (`stid`) REFERENCES `stocks` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buystocks`
--

LOCK TABLES `buystocks` WRITE;
/*!40000 ALTER TABLE `buystocks` DISABLE KEYS */;
INSERT INTO `buystocks` VALUES (1,32,1,'3M Company','Mon May 18 05:37:03 2020','135.99','1','135.99','pending'),(2,32,1,'3M Company','Wed May 20 00:01:13 2020','149.27','1','149.27','pending'),(3,31,4,'Abiomed, Inc.','Thu May 21 04:54:25 2020','190.79','1','190.79','pending'),(4,32,1,'3M Company','Thu May 21 19:49:11 2020','148.21','12','1778.52','pending'),(5,32,1,'3M Company','Thu May 21 20:16:40 2020','148.21','12','1778.52','pending'),(7,32,187,'Facebook, Inc.','Thu May 21 20:27:14 2020','229.97','1000','229970.00','payment failed'),(8,32,1,'3M Company','Thu May 21 20:35:04 2020','148.21','0','14821.00','payment successful'),(9,32,187,'Facebook, Inc.','Thu May 21 20:37:41 2020','229.97','100','22997.00','payment successful'),(10,32,1,'3M Company','Thu May 21 23:11:13 2020','148.21','90','14821.00','payment successful'),(11,32,453,'Twitter, Inc.','Thu May 21 23:54:02 2020','32.23','80','3223.00','payment successful'),(12,32,1,'3M Company','Fri May 22 00:58:10 2020','148.21','20','2964.20','payment successful'),(13,32,15,'Alaska Air Group, Inc.','Fri May 22 01:38:58 2020','30.26','0','302.60','payment successful'),(14,32,15,'Alaska Air Group, Inc.','Fri May 22 02:11:51 2020','30.26','0','605.20','payment successful');
/*!40000 ALTER TABLE `buystocks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-24 14:39:07
