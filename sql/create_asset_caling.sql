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

CREATE TABLE  `cabling_info` (
 `id` INT( 11 ) NOT NULL AUTO_INCREMENT ,
 `logic_device_name` VARCHAR( 255 ) NOT NULL ,
 `physical_location` VARCHAR( 255 ) NOT NULL ,
 `mac_addr` VARCHAR( 22 ) DEFAULT NULL ,
 `switch` VARCHAR( 255 ) NOT NULL ,
 `interface` VARCHAR( 255 ) NOT NULL ,
 `port_mode_speed` VARCHAR( 255 ) NOT NULL ,
 `functionality` VARCHAR( 255 ) NOT NULL ,
 `vlan_id` VARCHAR( 255 ) NOT NULL ,
 `FQDN` VARCHAR( 255 ) NOT NULL ,
 `ip_addr` VARCHAR( 255 ) NOT NULL ,
 `rack_location` VARCHAR( 255 ) DEFAULT NULL ,
 `server_name` VARCHAR( 255 ) NOT NULL ,
PRIMARY KEY (  `id` ) ,
UNIQUE KEY  `interface` (  `interface` ,  `FQDN` )
) ENGINE = INNODB DEFAULT CHARSET = utf8;


