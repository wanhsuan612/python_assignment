CREATE DATABASE IF NOT EXISTS python_assignment;

use python_assignment;

DROP TABLE IF EXISTS `financial_data`;
CREATE TABLE `financial_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `open_price` varchar(10) DEFAULT NULL,
  `close_price` varchar(10) DEFAULT NULL,
  `volume` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `symbol_date` (`symbol`,`date`)
);
