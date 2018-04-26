DROP TABLE IF EXISTS `bus`.`account`;
CREATE TABLE  `bus`.`account` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ACCOUNT_ID` varchar(45) NOT NULL,
  `ACCOUNT_TYPE` varchar(45) NOT NULL,
  `USER_ID` varchar(45) NOT NULL,
  `BALANCE` decimal(10,0) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `bus`.`order`;
CREATE TABLE  `bus`.`order` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ORDER_ID` varchar(45) NOT NULL,
  `ORDER_TYPE` varchar(45) NOT NULL,
  `FROM_USER_ID` varchar(45) NOT NULL,
  `AMOUNT` decimal(10,0) NOT NULL,
  `TO_USER_ID` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `bus`.`user`;
CREATE TABLE  `bus`.`user` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(45) NOT NULL,
  `USER_NAME` varchar(45) NOT NULL,
  `SEX` varchar(2) NOT NULL,
  `CARD_NUM` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;