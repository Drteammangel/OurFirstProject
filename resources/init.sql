/*create database spider*/
CREATE DATABASE IF NOT EXISTS `spider` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;

USE `spider`;

/*create table raw_data*/
DROP TABLE IF EXISTS `raw_data`;
CREATE TABLE IF NOT EXISTS `raw_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `url` varchar(255) COLLATE utf8_bin NOT NULL COMMENT '原始网页地址',
  `data` TEXT NOT NULL COMMENT '原始网页数据',
  `column` int(11) DEFAULT NULL COMMENT '预留字段',
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`),
  KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='原始数据表' AUTO_INCREMENT=1 ;