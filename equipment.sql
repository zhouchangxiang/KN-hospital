/*
Navicat MySQL Data Transfer

Source Server         : hstl2
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : hstl

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2021-01-11 16:07:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `equipment`
-- ----------------------------
DROP TABLE IF EXISTS `equipment`;
CREATE TABLE `equipment` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `EquipmentNo` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `EquipmentCode` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `EquipmentType` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
  `EquipmentModel` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
  `EquipmentName` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Floor` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Area` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `AddTime` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Status` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Comment` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Manufacturer` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ManufacturerUser` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ManufacturerPhone` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `KeepCompany` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `KeepUser` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `KeepPhone` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `RepairCompany` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `RepairUser` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `RepairPhone` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of equipment
-- ----------------------------
INSERT INTO `equipment` VALUES ('1', '16', 'SAC0001', '制冷设备', null, '空调1', '厚德楼9楼', '厚德楼9楼病人活动区', '2019-03-04 02:08:08', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('2', '18', 'SAC0003', '制冷设备', null, '空调3', '厚德楼9楼', '厚德楼9楼病人活动区', '2019-03-04 02:08:08', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('3', '19', 'SAC0004', '制冷设备', null, '空调4', '厚德楼9楼', '厚德楼9楼配餐室', '2019-03-04 02:12:11', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('4', '20', 'SAC0005', '制冷设备', null, '空调5', '厚德楼9楼', '厚德楼9楼901', '2019-03-04 02:15:22', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('5', '21', 'SAC0006', '制冷设备', null, '空调6', '厚德楼9楼', '厚德楼9楼902', '2019-03-04 02:15:22', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('6', '22', 'SAC0007', '制冷设备', null, '空调7', '厚德楼9楼', '厚德楼9楼903', '2019-03-04 02:15:22', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('7', '23', 'SAC0008', '制冷设备', null, '空调8', '厚德楼9楼', '厚德楼9楼903', '2019-03-04 02:15:22', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('8', '24', 'SAC0009', '制冷设备', null, '空调9', '厚德楼9楼', '厚德楼9楼903', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('9', '25', 'SAC0010', '制冷设备', null, '空调10', '厚德楼9楼', '厚德楼9楼904', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('10', '26', 'SAC0011', '制冷设备', null, '空调11', '厚德楼9楼', '厚德楼9楼905', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('11', '27', 'SAC0013', '制冷设备', null, '空调13', '厚德楼9楼', '厚德楼9楼906', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('12', '28', 'SAC0014', '制冷设备', null, '空调14', '厚德楼9楼', '厚德楼9楼907', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('13', '29', 'SAC0015', '制冷设备', null, '空调15', '厚德楼9楼', '厚德楼9楼908', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('14', '30', 'SAC0016', '制冷设备', null, '空调16', '厚德楼9楼', '厚德楼9楼909', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('15', '31', 'SAC0012', '制冷设备', null, '空调12', '厚德楼9楼', '厚德楼9楼905', '2019-03-04 02:23:44', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('16', '32', 'SAC0022', '制冷设备', null, '空调22', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:25:54', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('17', '33', 'SAC0023', '制冷设备', null, '空调23', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:25:54', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('18', '34', 'SAC0024', '制冷设备', null, '空调24', '厚德楼9楼', '厚德楼9楼护士站', '2019-03-04 02:25:54', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('19', '35', 'SAC0025', '制冷设备', null, '空调25', '厚德楼9楼', '厚德楼9楼电梯厅', '2019-03-04 02:25:54', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('20', '36', 'SAC0026', '制冷设备', null, '空调26', '厚德楼9楼', '厚德楼9楼办公区走道', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('21', '37', 'SAC0027', '制冷设备', null, '空调27', '厚德楼9楼', '厚德楼9楼护士办公室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('22', '38', 'SAC0028', '制冷设备', null, '空调28', '厚德楼9楼', '厚德楼9楼治疗室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('23', '39', 'SAC0029', '制冷设备', null, '空调29', '厚德楼9楼', '厚德楼9楼抢救室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('24', '40', 'SAC0030', '制冷设备', null, '空调30', '厚德楼9楼', '厚德楼9楼医生办公室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('25', '41', 'SAC0031', '制冷设备', null, '空调31', '厚德楼9楼', '厚德楼9楼医生办公室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('26', '42', 'SAC0032', '制冷设备', null, '空调32', '厚德楼9楼', '厚德楼9楼茶歇室', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('27', '43', 'SAC0017', '制冷设备', null, '空调17', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('28', '44', 'SAC0018', '制冷设备', null, '空调18', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('29', '45', 'SAC0019', '制冷设备', null, '空调19', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('30', '46', 'SAC0020', '制冷设备', null, '空调20', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('31', '47', 'SAC0021', '制冷设备', null, '空调21', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:25:55', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('32', '48', 'SAC0033', '制冷设备', null, '空调33', '厚德楼9楼', '厚德楼9楼主任办公室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('33', '49', 'SAC0034', '制冷设备', null, '空调34', '厚德楼9楼', '厚德楼9楼病房1', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('34', '50', 'SAC0035', '制冷设备', null, '空调35', '厚德楼9楼', '厚德楼9楼病房2', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('35', '51', 'SAC0036', '制冷设备', null, '空调36', '厚德楼9楼', '厚德楼9楼医生值班室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('36', '52', 'SAC0037', '制冷设备', null, '空调37', '厚德楼9楼', '厚德楼9楼护士值班室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('37', '53', 'SAC0038', '制冷设备', null, '空调38', '厚德楼9楼', '厚德楼9楼护士更衣室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('38', '54', 'SAC0039', '制冷设备', null, '空调39', '厚德楼9楼', '厚德楼9楼示教室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('39', '55', 'SAC0040', '制冷设备', null, '空调40', '厚德楼9楼', '厚德楼9楼晤谈室', '2019-03-04 02:28:49', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('40', '56', 'LIGHT0001', '照明设备', null, '灯1', '厚德楼9楼', '厚德楼9楼病人活动区', '2019-03-04 02:30:19', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('41', '57', 'LIGHT0002', '照明设备', null, '灯2', '厚德楼9楼', '厚德楼9楼配餐室', '2019-03-04 02:31:08', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('42', '58', 'LIGHT0003', '照明设备', null, '灯3', '厚德楼9楼', '厚德楼9楼901', '2019-03-04 02:31:59', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('43', '59', 'LIGHT0004', '照明设备', null, '灯4', '厚德楼9楼', '厚德楼9楼902', '2019-03-04 02:31:59', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('44', '60', 'LIGHT0006', '照明设备', null, '灯6', '厚德楼9楼', '厚德楼9楼903', '2019-03-04 02:32:47', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('45', '61', 'LIGHT0007', '照明设备', null, '灯7', '厚德楼9楼', '厚德楼9楼904', '2019-03-04 02:32:47', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('46', '62', 'LIGHT0008', '照明设备', null, '灯8', '厚德楼9楼', '厚德楼9楼905', '2019-03-04 02:32:47', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('47', '63', 'LIGHT0005', '照明设备', null, '灯5', '厚德楼9楼', '厚德楼9楼903', '2019-03-04 02:32:47', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('48', '64', 'LIGHT0009', '照明设备', null, '灯9', '厚德楼9楼', '厚德楼9楼906', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('49', '65', 'LIGHT0010', '照明设备', null, '灯10', '厚德楼9楼', '厚德楼9楼907', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('50', '66', 'LIGHT0011', '照明设备', null, '灯11', '厚德楼9楼', '厚德楼9楼908', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('51', '67', 'LIGHT0012', '照明设备', null, '灯12', '厚德楼9楼', '厚德楼9楼909', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('52', '68', 'LIGHT0013', '照明设备', null, '灯13', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('53', '69', 'LIGHT0014', '照明设备', null, '灯14', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('54', '70', 'LIGHT0015', '照明设备', null, '灯15', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('55', '71', 'LIGHT0016', '照明设备', null, '灯16', '厚德楼9楼', '厚德楼9楼910', '2019-03-04 02:34:01', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('56', '72', 'LIGHT0029', '照明设备', null, '灯29', '厚德楼9楼', '厚德楼9楼护士办公室', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('57', '73', 'LIGHT0030', '照明设备', null, '灯30', '厚德楼9楼', '厚德楼9楼治疗室', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('58', '74', 'LIGHT0031', '照明设备', null, '灯31', '厚德楼9楼', '厚德楼9楼抢救室', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('59', '75', 'LIGHT0032', '照明设备', null, '灯32', '厚德楼9楼', '厚德楼9楼医生办公室', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('60', '76', 'LIGHT0017', '照明设备', null, '灯17', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('61', '77', 'LIGHT0018', '照明设备', null, '灯18', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('62', '78', 'LIGHT0019', '照明设备', null, '灯19', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('63', '79', 'LIGHT0020', '照明设备', null, '灯20', '厚德楼9楼', '厚德楼9楼病人区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('64', '80', 'LIGHT0021', '照明设备', null, '灯21', '厚德楼9楼', '厚德楼9楼护士站', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('65', '81', 'LIGHT0022', '照明设备', null, '灯22', '厚德楼9楼', '厚德楼9楼护士站', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('66', '82', 'LIGHT0023', '照明设备', null, '灯23', '厚德楼9楼', '厚德楼9楼护士站', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('67', '83', 'LIGHT0024', '照明设备', null, '灯24', '厚德楼9楼', '厚德楼9楼办公区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('68', '84', 'LIGHT0025', '照明设备', null, '灯25', '厚德楼9楼', '厚德楼9楼办公区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('69', '85', 'LIGHT0026', '照明设备', null, '灯26', '厚德楼9楼', '厚德楼9楼办公区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('70', '86', 'LIGHT0027', '照明设备', null, '灯27', '厚德楼9楼', '厚德楼9楼办公区走道', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('71', '87', 'LIGHT0028', '照明设备', null, '灯28', '厚德楼9楼', '厚德楼9楼电梯厅', '2019-03-04 02:36:27', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('72', '88', 'LIGHT0033', '照明设备', null, '灯33', '厚德楼9楼', '厚德楼9楼洗涤间', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('73', '89', 'LIGHT0034', '照明设备', null, '灯34', '厚德楼9楼', '厚德楼9楼污洗间', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('74', '90', 'LIGHT0035', '照明设备', null, '灯35', '厚德楼9楼', '厚德楼9楼茶歇室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('75', '91', 'LIGHT0036', '照明设备', null, '灯36', '厚德楼9楼', '厚德楼9楼主任办公室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('76', '92', 'LIGHT0037', '照明设备', null, '灯37', '厚德楼9楼', '厚德楼9楼病房1', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('77', '93', 'LIGHT0038', '照明设备', null, '灯38', '厚德楼9楼', '厚德楼9楼病房2', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('78', '94', 'LIGHT0039', '照明设备', null, '灯39', '厚德楼9楼', '厚德楼9楼医生值班室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('79', '95', 'LIGHT0040', '照明设备', null, '灯40', '厚德楼9楼', '厚德楼9楼护士值班室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('80', '96', 'LIGHT0041', '照明设备', null, '灯41', '厚德楼9楼', '厚德楼9楼护士更衣室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('81', '97', 'LIGHT0043', '照明设备', null, '灯43', '厚德楼9楼', '厚德楼9楼示教室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('82', '98', 'LIGHT0044', '照明设备', null, '灯44', '厚德楼9楼', '厚德楼9楼晤谈室', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('83', '99', 'LIGHT0042', '照明设备', null, '灯42', '厚德楼9楼', '厚德楼9楼库房', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('84', '100', 'LIGHT0045', '照明设备', null, '灯45', '厚德楼9楼', '厚德楼9楼护士站', '2019-03-04 02:39:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('85', '101', 'DB0001', '电表', null, '电表1', '厚德楼1楼', '厚德楼1楼强电井', '2019-03-04 02:40:18', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('86', '102', 'DB0002', '电表', null, '电表2', '厚德楼2楼', '厚德楼2楼强电井', '2019-03-04 02:41:14', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('87', '103', 'DB0003', '电表', null, '电表3', '厚德楼3楼', '厚德楼3楼强电井', '2019-03-04 02:42:45', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('88', '104', 'DB0004', '电表', null, '电表4', '厚德楼4楼', '厚德楼4楼强电井', '2019-03-04 02:42:45', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('89', '106', 'DB0005', '电表', null, '电表5', '厚德楼5楼', '厚德楼5楼强电井', '2019-03-04 02:43:15', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('90', '107', 'DB0006', '电表', null, '电表6', '厚德楼6楼', '厚德楼6楼强电井', '2019-03-04 02:43:15', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('91', '108', 'DB0007', '电表', null, '电表7', '厚德楼7楼', '厚德楼7楼强电井', '2019-03-04 02:43:15', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('92', '109', 'DB0008', '电表', null, '电表8', '厚德楼8楼', '厚德楼8楼强电井', '2019-03-04 02:43:15', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('93', '110', 'DB0009', '电表', null, '电表9', '厚德楼9楼', '厚德楼9楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('94', '111', 'DB0010', '电表', null, '电表10', '厚德楼10楼', '厚德楼10楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('95', '112', 'DB0011', '电表', null, '电表11', '厚德楼11楼', '厚德楼11楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('96', '113', 'DB0012', '电表', null, '电表12', '厚德楼12楼', '厚德楼12楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('97', '114', 'DB0013', '电表', null, '电表13', '厚德楼1楼', '厚德楼1楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('98', '115', 'DB0014', '电表', null, '电表14', '厚德楼2楼', '厚德楼2楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('99', '116', 'DB0015', '电表', null, '电表15', '厚德楼3楼', '厚德楼3楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('100', '117', 'DB0016', '电表', null, '电表16', '厚德楼4楼', '厚德楼4楼强电井', '2019-03-04 02:44:06', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('101', '118', 'DB0017', '电表', null, '电表17', '厚德楼5楼', '厚德楼5楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('102', '119', 'DB0018', '电表', null, '电表18', '厚德楼6楼', '厚德楼6楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('103', '120', 'DB0019', '电表', null, '电表19', '厚德楼7楼', '厚德楼7楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('104', '121', 'DB0020', '电表', null, '电表20', '厚德楼8楼', '厚德楼8楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('105', '122', 'DB0021', '电表', null, '电表21', '厚德楼9楼', '厚德楼9楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('106', '123', 'DB0022', '电表', null, '电表22', '厚德楼10楼', '厚德楼10楼强电井', '2019-03-04 02:45:28', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('107', '124', 'DB0023', '电表', null, '电表23', '厚德楼11楼', '厚德楼11楼强电井', '2019-03-04 02:45:29', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('108', '125', 'DB0024', '电表', null, '电表24', '厚德楼12楼', '厚德楼12楼强电井', '2019-03-04 02:45:29', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('109', '126', 'DB0025', '电表', null, '电表25', '厚德楼-1楼', '厚德楼-1楼配电房', '2019-03-04 02:45:29', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('110', '127', 'DB0026', '电表', null, '电表26', '厚德楼-1楼', '厚德楼-1楼配电房', '2019-03-04 02:45:29', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('111', '128', 'DB0027', '电表', null, '电表27', '厚德楼-1楼', '厚德楼-1楼空调机房', '2019-03-04 02:45:29', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('112', '129', 'SB0001', '水表', null, '水表1', '厚德楼9楼', '厚德楼9楼水管井', '2019-03-04 02:48:20', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('113', '130', 'SB0002', '水表', null, '水表2', '厚德楼8楼', '厚德楼8楼水管井', '2019-03-04 02:48:47', '正常', null, null, null, null, null, null, null, null, null, null);
INSERT INTO `equipment` VALUES ('114', '131', 'SAC001', '制冷设备', null, '空调2', '厚德楼1楼', '厚德楼1楼强电井', '2019-05-07 15:26:15', '正常', null, null, null, null, null, null, null, null, null, null);
