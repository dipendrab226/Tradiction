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
-- Table structure for table `traderreg`
--

DROP TABLE IF EXISTS `traderreg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traderreg` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `phoneno` varchar(45) NOT NULL,
  `ssnno` varchar(45) NOT NULL,
  `bankst` varchar(45) NOT NULL,
  `routingno` varchar(45) NOT NULL,
  `accountno` varchar(45) NOT NULL,
  `lid` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `lid_idx` (`lid`),
  CONSTRAINT `lid` FOREIGN KEY (`lid`) REFERENCES `login` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traderreg`
--

LOCK TABLES `traderreg` WRITE;
/*!40000 ALTER TABLE `traderreg` DISABLE KEYS */;
INSERT INTO `traderreg` VALUES (5,'Sanjay','Mirani','2306 33rd Avenue','San Francisco','California','4154259203','ikbFRmVd+XS+LJV6VjDA5Pv/0eVP9wYmeqYj4jXXWmg=','/media/SanjayMirani_bankstatement.jpg','EUxDstFJeX6tZNYySXLWJs+LE0gkLb3QZaR2xMk+big=','2EhJAlUNDlzYEi7fAm+TpsQqy499I5gtd15PIhbd1sY=',31,'Accepted'),(6,'Brian','Lim','88 Belhaven Court','Daly City','CALIFORNIA','4152603533','Ax2+uiLz/dJdeb4XS5t44WzT121SUVfajY/7hGjZS7g=','/media/BrianLim_bankstatement.png','miASxMvta9wy59hHM/1BaAfQ6+xr0gkwCB1bp95vkcA=','gJR5W9t+1yffCaDrDTWq9DVdSEyBO/tqdZ57ehnR6zw=',32,'Accepted'),(7,'Brian','Test','12 test ave.','Test','CA','123 123 1234','x2XfURNxhfpVeASsM/nCH6qYoUsgZX5cfc6QhUCPaOk=','/media/BrianTest_bankstatement.pdf','79uox1bRTf85GHxE7CpKFJJzK5U7LReSeAxdQLJW7kk=','M6dAZEQyHpS7h27fKnAlk+FwMKKQrQTj6IrbdqiVKZw=',33,'pending');
/*!40000 ALTER TABLE `traderreg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-24 14:39:04
