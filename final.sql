/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - orphanage
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`orphanage` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `orphanage`;

/*Table structure for table `adoption_request` */

DROP TABLE IF EXISTS `adoption_request`;

CREATE TABLE `adoption_request` (
  `adoption_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `orphan_id` int(11) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`adoption_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `adoption_request` */

insert  into `adoption_request`(`adoption_request_id`,`user_id`,`orphan_id`,`description`,`datetime`,`status`) values 
(1,1,2,'intersted in adopting','2022-08-01 14:52:42','accept'),
(3,1,1,'intersted in adopting','2023-05-15 14:58:05','accept'),
(4,1,2,'testing','2023-06-01 09:55:40','accept'),
(6,4,3,'testing asdf','2023-06-01 09:57:40','accept'),
(8,4,6,'intersted in adopting','2023-06-02 12:20:39','accept'),
(9,4,6,'intersted in adopting','2023-06-02 12:54:57','accept'),
(10,4,3,'abc','2023-06-02 12:55:41','accept'),
(11,5,6,'intersted in adopting','2023-06-02 13:00:32','pending'),
(12,5,6,'intersted in adopting','2023-06-02 13:07:24','pending'),
(13,8,7,'jhujh','2023-06-02 13:12:19','accept'),
(14,8,6,'ssssssssssssss','2024-02-29 22:57:34','pending'),
(15,9,8,'zxca','2024-03-01 08:54:55','pending'),
(16,9,6,'jshgdf','2024-03-01 08:58:15','pending');

/*Table structure for table `donations` */

DROP TABLE IF EXISTS `donations`;

CREATE TABLE `donations` (
  `donation_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `requirement_id` int(11) DEFAULT NULL,
  `amount` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`donation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `donations` */

insert  into `donations`(`donation_id`,`user_id`,`requirement_id`,`amount`,`datetime`) values 
(1,1,NULL,'30,000','2022-08-01 14:52:10'),
(2,2,NULL,'10,000','2022-08-01 14:59:32'),
(3,4,NULL,'30000','2022-08-13 11:26:26'),
(4,1,NULL,'30,000','2022-08-19 10:27:00'),
(5,4,4,'30000','2022-08-19 12:40:32'),
(6,4,4,'30000','2022-08-19 12:41:40'),
(7,1,5,'30000','2023-05-15 14:59:50'),
(8,1,9,'10,000','2023-05-15 15:05:01'),
(9,1,11,'','2023-05-16 00:03:34'),
(10,4,13,'7777','2023-06-01 09:23:59'),
(11,5,12,'5000','2023-06-02 09:39:25');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_title` varchar(40) DEFAULT NULL,
  `venue` varchar(40) DEFAULT NULL,
  `date_and_time` varchar(40) DEFAULT NULL,
  `chief_guest` varchar(40) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `event_status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `event` */

insert  into `event`(`event_id`,`event_title`,`venue`,`date_and_time`,`chief_guest`,`description`,`event_status`) values 
(1,'charity book fair','orphanage main hall','2022-08-19T17:00','ernakulam collector ','anyone can buy or participate in the eve','event added'),
(2,'testing','testing','2023-05-02T09:49','testing','testing','event added'),
(7,'asdgg','hall','2023-06-15','mathew','descri','event added');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`description`,`datetime`) values 
(1,2,'good','2022-08-01 15:22:47'),
(2,5,'abcd','2022-08-21 10:36:51'),
(3,5,'','2023-06-01 09:18:51'),
(4,5,'very good in organising','2023-06-01 09:19:19'),
(5,5,'','2023-06-01 13:08:32'),
(6,5,'','2023-06-01 13:09:34');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'fawas','fawas','user'),
(3,'dona','dona','user'),
(4,'safeera','safeera','user'),
(5,'asdf','asdf','user'),
(6,'clint','clint','user'),
(7,'asd','asd','user'),
(8,'asd','asd','user'),
(9,'mathew','mathew','user'),
(10,'hai','hai','orphanage'),
(11,'dris','dris','user');

/*Table structure for table `orphanage` */

DROP TABLE IF EXISTS `orphanage`;

CREATE TABLE `orphanage` (
  `orphanage_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` varchar(40) DEFAULT NULL,
  `orphanage_name` varchar(40) DEFAULT NULL,
  `place_name` varchar(40) DEFAULT NULL,
  `pincode` varchar(40) DEFAULT NULL,
  `district` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `adoption_criteria` varchar(40) DEFAULT NULL,
  `sponsoring_criteria` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`orphanage_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `orphanage` */

insert  into `orphanage`(`orphanage_id`,`login_id`,`orphanage_name`,`place_name`,`pincode`,`district`,`phone`,`email`,`adoption_criteria`,`sponsoring_criteria`) values 
(1,'10','hai','kerala','682032','mumbai','02345678907','renukakamath2@gmail.com','sdad','sadas');

/*Table structure for table `orphans` */

DROP TABLE IF EXISTS `orphans`;

CREATE TABLE `orphans` (
  `orphan_id` int(11) NOT NULL AUTO_INCREMENT,
  `orphanage_id` int(40) DEFAULT NULL,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `dob` varchar(40) DEFAULT NULL,
  `orphan_image` int(11) DEFAULT NULL,
  `gender` varchar(40) DEFAULT NULL,
  `about_description` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`orphan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `orphans` */

insert  into `orphans`(`orphan_id`,`orphanage_id`,`first_name`,`last_name`,`dob`,`orphan_image`,`gender`,`about_description`) values 
(2,1,'aleena ','joy','2019-03-09',3,'female','3 year old child '),
(3,1,'keerthik','s','2021-03-09',11,'male','infant '),
(5,1,'jacob','p','2022-11-17',12,'male','infant male '),
(6,1,'abcd','qwre','2023-05-19',5,'female','tryty'),
(7,1,'fawas','sakeer','2023-03-25',8,'male','abcdefghijkalmnop'),
(8,10,'sdf','asfas','2024-01-30',10,'male','asda');

/*Table structure for table `requirements` */

DROP TABLE IF EXISTS `requirements`;

CREATE TABLE `requirements` (
  `requirement_id` int(11) NOT NULL AUTO_INCREMENT,
  `orphanage_id` int(11) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`requirement_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

/*Data for the table `requirements` */

insert  into `requirements`(`requirement_id`,`orphanage_id`,`description`,`datetime`,`status`) values 
(5,1,'rs 10,000 for food ','2022-08-01 14:49:22','donated'),
(9,1,'1000','2023-05-15 15:03:03','donated'),
(11,1,'1000','2023-05-15 23:43:36','donated'),
(12,1,'rs 5000','2023-05-16 00:05:17','donated'),
(22,1,'bus','2023-06-02 12:16:15','accept'),
(23,10,'jjk','2024-02-22 11:03:01','accept'),
(24,10,'chairs (100)','2024-02-27 14:45:23','pending');

/*Table structure for table `sponsor_requests` */

DROP TABLE IF EXISTS `sponsor_requests`;

CREATE TABLE `sponsor_requests` (
  `sponsor_req_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `orphan_id` int(11) DEFAULT NULL,
  `contribution_details` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`sponsor_req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `sponsor_requests` */

insert  into `sponsor_requests`(`sponsor_req_id`,`user_id`,`orphan_id`,`contribution_details`,`datetime`,`status`) values 
(1,1,1,'study materials for 1 year','2022-08-01 14:53:13','accept'),
(2,2,1,'study materuals','2022-08-01 15:00:55','pending'),
(3,1,2,'testing','2023-06-01 09:54:08','pending'),
(4,4,2,'study materuals','2023-06-01 12:58:36','pending'),
(5,2,2,'bvv','2024-02-27 16:08:45','pending');

/*Table structure for table `teaching_requests` */

DROP TABLE IF EXISTS `teaching_requests`;

CREATE TABLE `teaching_requests` (
  `teaching_req_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  `datetime` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`teaching_req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `teaching_requests` */

insert  into `teaching_requests`(`teaching_req_id`,`user_id`,`description`,`datetime`,`status`) values 
(1,1,'interested in teaching math for 2 hours ','2022-08-01 14:47:29','accept'),
(2,2,'interested in teaching basic evironmenta','2022-08-01 14:58:15','pending');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(40) DEFAULT NULL,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `gender` varchar(40) DEFAULT NULL,
  `house_name` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `occupation` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`gender`,`house_name`,`place`,`phone`,`email`,`occupation`) values 
(1,2,'fawas','sakeer','male','cc33/612A2','vennala','8086626374','fawas@gmail.com','business'),
(2,3,'dona','justine','female','324A','thengode','9447043124','dona@gmail.com','business'),
(3,4,'safeera','zaman','female','17C','elamakkara','9745037364','safeera05@gmail.com','scientist'),
(4,5,'asdf','asdf','male','asdf','asdf','1234567899','sszs@s.com','s'),
(5,6,'sebastian','yantra','male','clint h','california','1234567890','clint@gmail.com','engineer'),
(6,7,'fawas','raun','male','VETTICKAL HOUSE, VENNALA PO','thengode','8086626374','dona@gmail.com','teacher'),
(7,8,'fawas','raun','male','VETTICKAL HOUSE, VENNALA PO','thengode','8086626374','dona@gmail.com','teacher'),
(8,9,'mathew','cd','male','18a','kl','1234543212','matt@gmail.com','engg'),
(9,11,'drisya','dinesh','female','kalayath','pachalam','9188354235','drisya@gmail.com','teacher');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
