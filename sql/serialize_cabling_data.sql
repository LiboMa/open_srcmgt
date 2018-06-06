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


insert into cabling_info (rack, device_name, he, card, slot, port, device_type, cable_id, vlan_id, func,updated_on,created_on)values("Server13","FSCNBEUL9009","7-8","onboard","","ILO","server","A0061","32","ILO",now(),now());

insert into cabling_info (rack, device_name, he, card, slot, port, device_type, cable_id, vlan_id, func,updated_on,created_on)values("Server13","i04101","36","105","47","ILO","server","A0061","314","ILO",now(),now()); 

# update child_id based on cable_id

update cabling_info as server, (select id,cable_id from cabling_info where device_type="switch") as switch set server.child_id = switch.id where server.cable_id = switch.cable_id and server.device_type="server";

# update parent_id based on cable_id
update cabling_info as child, (select id,cable_id from cabling_info where device_type="server") as server set child.parent_id = server.id where child.cable_id = server.cable_id and child.device_type !="server";
