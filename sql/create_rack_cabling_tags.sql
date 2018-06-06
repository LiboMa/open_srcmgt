CREATE TABLE asset (
id int(11) NOT NULL AUTO_INCREMENT,
logic_name varchar(255) NOT NULL,
device_type varchar(255) NOT NULL,
serial_number varchar(10) NOT NULL,
hardware_info text,
layout varchar(255),
status varchar(30),
history text,
PRIMARY KEY(id),
updated_on datetime
) ENGINE = INNODB DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `cabling_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cable_id` varchar(255) NOT NULL,
  `device_name` varchar(255) NOT NULL,
  `device_type` varchar(255) DEFAULT NULL,
  `rack` varchar(255) NOT NULL,
  `he` varchar(255) NOT NULL,
  `card` varchar(22) DEFAULT NULL,
  `slot` varchar(255) DEFAULT NULL,
  `port` varchar(255) DEFAULT NULL,
  `vlan_id` varchar(255) DEFAULT NULL,
  `func` varchar(255) DEFAULT NULL,
  `parent_id` int(255) DEFAULT NULL,
  `child_id` int(255) DEFAULT NULL,
  `comment_1` varchar(255) DEFAULT NULL,
  `comment_2` varchar(255) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `parent_id` (`parent_id`),
  UNIQUE KEY `child_id` (`child_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;



#UNIQUE KEY  `interface` (  `interface` ,  `FQDN` )

CREATE TABLE  `cabling_rack` (
 `id` INT( 11 ) NOT NULL AUTO_INCREMENT ,
 `name` VARCHAR( 255 ) NOT NULL ,
 `capacity` VARCHAR( 255 ) NOT NULL ,
 `datacenter` VARCHAR( 255 ) DEFAULT NULL ,
 `updated_on` datetime,
 `created_on` datetime,
 `comment_1` VARCHAR( 255 ) NOT NULL ,
 `comment_2` VARCHAR( 255 ) NOT NULL ,
 `comment_3` VARCHAR( 255 ) NOT NULL ,
PRIMARY KEY (  `id` ) ,
UNIQUE KEY  `name` (`name`)
) ENGINE = INNODB DEFAULT CHARSET = utf8;

