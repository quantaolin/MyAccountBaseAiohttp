DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ACCOUNT_ID` varchar(45) NOT NULL,
  `ACCOUNT_TYPE` varchar(45) NOT NULL,
  `USER_ID` varchar(45) NOT NULL,
  `BALANCE` decimal(10,0) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `IDEX_ACCOUNT_ID` (`ACCOUNT_ID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ORDER_ID` varchar(45) NOT NULL,
  `ORDER_TYPE` varchar(45) NOT NULL,
  `FROM_USER_ID` varchar(45),
  `AMOUNT` decimal(10,0) NOT NULL,
  `TO_USER_ID` varchar(45),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `IDEX_ORDER_ID` (`ORDER_ID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(45) NOT NULL,
  `USER_NAME` varchar(45) NOT NULL,
  `SEX` varchar(2) NOT NULL,
  `CARD_NUM` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `IDEX_USER_ID` (`USER_ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;