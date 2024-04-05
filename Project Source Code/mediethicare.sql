-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 11, 2024 at 11:39 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mediethicare`
--
CREATE DATABASE IF NOT EXISTS `mediethicare` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `mediethicare`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add hospital', 7, 'add_hospital'),
(26, 'Can change hospital', 7, 'change_hospital'),
(27, 'Can delete hospital', 7, 'delete_hospital'),
(28, 'Can view hospital', 7, 'view_hospital'),
(29, 'Can add medicine', 8, 'add_medicine'),
(30, 'Can change medicine', 8, 'change_medicine'),
(31, 'Can delete medicine', 8, 'delete_medicine'),
(32, 'Can view medicine', 8, 'view_medicine'),
(33, 'Can add bed availability', 9, 'add_bedavailability'),
(34, 'Can change bed availability', 9, 'change_bedavailability'),
(35, 'Can delete bed availability', 9, 'delete_bedavailability'),
(36, 'Can view bed availability', 9, 'view_bedavailability'),
(37, 'Can add doctor availability', 10, 'add_doctoravailability'),
(38, 'Can change doctor availability', 10, 'change_doctoravailability'),
(39, 'Can delete doctor availability', 10, 'delete_doctoravailability'),
(40, 'Can view doctor availability', 10, 'view_doctoravailability'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user'),
(45, 'Can add appointment', 12, 'add_appointment'),
(46, 'Can change appointment', 12, 'change_appointment'),
(47, 'Can delete appointment', 12, 'delete_appointment'),
(48, 'Can view appointment', 12, 'view_appointment'),
(49, 'Can add surgical service', 13, 'add_surgicalservice'),
(50, 'Can change surgical service', 13, 'change_surgicalservice'),
(51, 'Can delete surgical service', 13, 'delete_surgicalservice'),
(52, 'Can view surgical service', 13, 'view_surgicalservice'),
(53, 'Can add emergency service', 14, 'add_emergencyservice'),
(54, 'Can change emergency service', 14, 'change_emergencyservice'),
(55, 'Can delete emergency service', 14, 'delete_emergencyservice'),
(56, 'Can view emergency service', 14, 'view_emergencyservice'),
(57, 'Can add diagnostic service', 15, 'add_diagnosticservice'),
(58, 'Can change diagnostic service', 15, 'change_diagnosticservice'),
(59, 'Can delete diagnostic service', 15, 'delete_diagnosticservice'),
(60, 'Can view diagnostic service', 15, 'view_diagnosticservice'),
(61, 'Can add hospital report', 16, 'add_hospitalreport'),
(62, 'Can change hospital report', 16, 'change_hospitalreport'),
(63, 'Can delete hospital report', 16, 'delete_hospitalreport'),
(64, 'Can view hospital report', 16, 'view_hospitalreport'),
(65, 'Can add medicine blockchain', 17, 'add_medicineblockchain'),
(66, 'Can change medicine blockchain', 17, 'change_medicineblockchain'),
(67, 'Can delete medicine blockchain', 17, 'delete_medicineblockchain'),
(68, 'Can view medicine blockchain', 17, 'view_medicineblockchain'),
(69, 'Can add bk model', 18, 'add_bkmodel'),
(70, 'Can change bk model', 18, 'change_bkmodel'),
(71, 'Can delete bk model', 18, 'delete_bkmodel'),
(72, 'Can view bk model', 18, 'view_bkmodel'),
(73, 'Can add cart', 19, 'add_cart'),
(74, 'Can change cart', 19, 'change_cart'),
(75, 'Can delete cart', 19, 'delete_cart'),
(76, 'Can view cart', 19, 'view_cart'),
(77, 'Can add cart item', 20, 'add_cartitem'),
(78, 'Can change cart item', 20, 'change_cartitem'),
(79, 'Can delete cart item', 20, 'delete_cartitem'),
(80, 'Can view cart item', 20, 'view_cartitem'),
(81, 'Can add cart medicine', 21, 'add_cartmedicine'),
(82, 'Can change cart medicine', 21, 'change_cartmedicine'),
(83, 'Can delete cart medicine', 21, 'delete_cartmedicine'),
(84, 'Can view cart medicine', 21, 'view_cartmedicine'),
(85, 'Can add pending medicine', 22, 'add_pendingmedicine'),
(86, 'Can change pending medicine', 22, 'change_pendingmedicine'),
(87, 'Can delete pending medicine', 22, 'delete_pendingmedicine'),
(88, 'Can view pending medicine', 22, 'view_pendingmedicine');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blockchainmodel`
--

DROP TABLE IF EXISTS `blockchainmodel`;
CREATE TABLE IF NOT EXISTS `blockchainmodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `medicineid` varchar(100) NOT NULL,
  `medicine_price` varchar(100) NOT NULL,
  `medicine_type` varchar(100) NOT NULL,
  `medicine_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blockchainmodel_medicine_id_eb75f27e` (`medicine_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `blockchainmodel`
--

INSERT INTO `blockchainmodel` (`id`, `medicineid`, `medicine_price`, `medicine_type`, `medicine_id`) VALUES
(18, '7a61b53701befdae0eeeffaecc73f14e20b537bb0f8b91ad7c2936dc63562b25', '811786ad1ae74adfdd20dd0372abaaebc6246e343aebd01da0bfc4c02bf0106c', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', NULL),
(19, 'aea92132c4cbeb263e6ac2bf6c183b5d81737f179f21efdc5863739672f0f470', '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790', '51ee757a7bfb6307a6509aa21aedb4686816d2bd38229a710872adb6c1b2ac75', NULL),
(20, '0b918943df0962bc7a1824c0555a389347b4febdc7cf9d1254406d80ce44e3f9', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', NULL),
(17, '76a50887d8f1c2e9301755428990ad81479ee21c25b43215cf524541e0503269', '86e50149658661312a9e0b35558d84f6c6d3da797f552a9657fe0558ca40cdef', '51ee757a7bfb6307a6509aa21aedb4686816d2bd38229a710872adb6c1b2ac75', NULL),
(16, '9f14025af0065b30e47e23ebb3b491d39ae8ed17d33739e5ff3827ffb3634953', 'e29c9c180c6279b0b02abd6a1801c7c04082cf486ec027aa13515e4f3884bb6b', '352554262e2ad2308c2ebeca4b04f9227a30c71e94603a1c3d90beadc31f9bab', NULL),
(15, '86e50149658661312a9e0b35558d84f6c6d3da797f552a9657fe0558ca40cdef', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', NULL),
(14, 'c6f3ac57944a531490cd39902d0f777715fd005efac9a30622d5f5205e7f6894', '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', NULL),
(21, 'd59eced1ded07f84c145592f65bdf854358e009c5cd705f5215bf18697fed103', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', 40),
(22, '3d914f9348c9cc0ff8a79716700b9fcd4d2f3e711608004eb8f138bcba7f14d9', '6f4b6612125fb3a0daecd2799dfd6c9c299424fd920f9b308110a2c1fbd8f443', '51ee757a7bfb6307a6509aa21aedb4686816d2bd38229a710872adb6c1b2ac75', 41),
(23, '73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049', '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790', 'e34a879c8b8b67effd9e14878e1443829419cf2aba09a03252d2a4f137e49941', 42);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'hospitalapp', 'hospital'),
(8, 'hospitalapp', 'medicine'),
(9, 'hospitalapp', 'bedavailability'),
(10, 'hospitalapp', 'doctoravailability'),
(11, 'userapp', 'user'),
(12, 'userapp', 'appointment'),
(13, 'hospitalapp', 'surgicalservice'),
(14, 'hospitalapp', 'emergencyservice'),
(15, 'hospitalapp', 'diagnosticservice'),
(16, 'userapp', 'hospitalreport'),
(17, 'hospitalapp', 'medicineblockchain'),
(18, 'hospitalapp', 'bkmodel'),
(19, 'userapp', 'cart'),
(20, 'userapp', 'cartitem'),
(21, 'userapp', 'cartmedicine'),
(22, 'userapp', 'pendingmedicine');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-03 11:57:00.892428'),
(2, 'auth', '0001_initial', '2024-02-03 11:57:01.743976'),
(3, 'admin', '0001_initial', '2024-02-03 11:57:02.010808'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-03 11:57:02.020209'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-03 11:57:02.030494'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-03 11:57:02.133692'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-03 11:57:02.190370'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-03 11:57:02.249410'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-03 11:57:02.259097'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-03 11:57:02.305594'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-03 11:57:02.306597'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-03 11:57:02.315071'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-03 11:57:02.359428'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-03 11:57:02.405487'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-03 11:57:02.446222'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-03 11:57:02.458184'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-03 11:57:02.524863'),
(18, 'hospitalapp', '0001_initial', '2024-02-03 11:57:02.537611'),
(19, 'sessions', '0001_initial', '2024-02-03 11:57:02.584736'),
(20, 'hospitalapp', '0002_alter_hospital_otp_status', '2024-02-03 12:06:50.724219'),
(21, 'hospitalapp', '0003_alter_hospital_otp_alter_hospital_otp_status', '2024-02-03 12:07:39.617872'),
(22, 'hospitalapp', '0004_medicine', '2024-02-04 15:50:55.711692'),
(23, 'hospitalapp', '0005_medicine_date', '2024-02-04 16:39:05.157940'),
(24, 'hospitalapp', '0006_alter_medicine_date', '2024-02-04 16:39:56.023680'),
(25, 'hospitalapp', '0007_bedavailability', '2024-02-05 06:11:41.728132'),
(26, 'hospitalapp', '0008_doctoravailability', '2024-02-05 06:32:26.726389'),
(27, 'userapp', '0001_initial', '2024-02-05 06:54:12.309566'),
(28, 'userapp', '0002_appointment', '2024-02-05 10:18:59.032936'),
(29, 'userapp', '0003_appointment_name', '2024-02-05 10:36:02.095888'),
(30, 'hospitalapp', '0009_diagnosticservice_emergencyservice_surgicalservice', '2024-02-05 10:54:44.678449'),
(31, 'userapp', '0004_appointment_status', '2024-02-05 11:32:01.111773'),
(32, 'userapp', '0005_hospitalreport', '2024-02-07 06:02:12.425827'),
(33, 'userapp', '0006_user_medicines', '2024-02-07 06:52:50.263697'),
(34, 'userapp', '0007_alter_hospitalreport_appointment_date', '2024-02-07 10:13:19.639896'),
(35, 'userapp', '0008_user_allergies_user_blood_group_user_date_of_birth_and_more', '2024-02-07 10:46:43.907005'),
(36, 'hospitalapp', '0010_medicineblockchain', '2024-02-07 16:00:35.418632'),
(37, 'hospitalapp', '0011_delete_medicineblockchain', '2024-02-08 05:49:08.286774'),
(38, 'hospitalapp', '0012_bkmodel', '2024-02-08 05:51:08.957716'),
(39, 'hospitalapp', '0013_alter_bkmodel_medicine_price', '2024-02-08 07:00:46.555999'),
(40, 'hospitalapp', '0014_alter_bkmodel_medicine_price', '2024-02-08 07:01:55.420856'),
(41, 'hospitalapp', '0015_alter_medicine_medicine_price', '2024-02-08 07:02:34.988085'),
(42, 'userapp', '0009_cart', '2024-02-08 09:28:12.380855'),
(43, 'userapp', '0010_remove_cart_medicine_ids_cart_medicine_ids', '2024-02-08 09:39:46.181454'),
(44, 'userapp', '0011_delete_cart', '2024-02-08 09:44:44.770517'),
(45, 'hospitalapp', '0016_hospital_admin_status', '2024-02-08 10:53:29.011541'),
(46, 'hospitalapp', '0017_hospital_hospital_doc', '2024-02-08 10:59:34.202634'),
(47, 'userapp', '0012_cartitem', '2024-02-09 12:17:15.360052'),
(48, 'userapp', '0013_cart_cartmedicine_cart_medicines', '2024-02-09 15:55:52.026951'),
(49, 'userapp', '0014_remove_cartmedicine_cart_and_more', '2024-02-09 16:07:04.894691'),
(50, 'userapp', '0015_cartitem_status', '2024-02-09 16:08:12.635276'),
(51, 'userapp', '0016_pendingmedicine', '2024-02-09 17:58:38.658398'),
(52, 'userapp', '0017_cartitem_hospital_status', '2024-02-09 18:23:17.954537'),
(53, 'userapp', '0018_alter_hospitalreport_unethical_staff_name', '2024-02-10 19:48:10.384444'),
(54, 'userapp', '0019_alter_hospitalreport_unethical_staff_name', '2024-02-10 19:49:17.988410'),
(55, 'userapp', '0020_alter_user_status', '2024-02-11 08:30:46.211064'),
(56, 'userapp', '0021_alter_appointment_name_and_more', '2024-02-11 11:10:24.830923'),
(57, 'userapp', '0022_alter_hospitalreport_unethical_staff_name', '2024-02-11 11:10:24.903757'),
(58, 'userapp', '0023_alter_hospitalreport_unethical_staff_name', '2024-02-11 11:10:57.469663');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('eq8qngs1p1kyptvxzwbx2o8ffgezlq4y', 'eyJ1c2VyX2xvZ2luX2lkIjoxfQ:1rXJ8u:-mPwEBRi41zRw47ALsH0ulQ3z-zOG7zKeQ5WpeOwGaY', '2024-02-20 10:57:32.921779'),
('hbiw72kaa7m4iv31ozr3msan46uxmz6d', '.eJyrVsrILy7ILEnMic9MUbIy1UHwy1KLMtMyU1NgEqXFqUXxOfnpmXlgEUMdpeTEopL45PzSvBIlK4NaAAV3GqI:1rY2ZU:SoyJQ7zNaCMWoSc8TNO_YT2znNvSCmIgw1XLK6qB2Qw', '2024-02-22 11:28:00.558165');

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_bedavailability`
--

DROP TABLE IF EXISTS `hospitalapp_bedavailability`;
CREATE TABLE IF NOT EXISTS `hospitalapp_bedavailability` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bed_type` varchar(50) NOT NULL,
  `bed_price_per_day` decimal(10,2) NOT NULL,
  `bed_description` longtext NOT NULL,
  `num_beds_available` int NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_bedavailability_hospital_id_7f613b4d` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_bedavailability`
--

INSERT INTO `hospitalapp_bedavailability` (`id`, `bed_type`, `bed_price_per_day`, `bed_description`, `num_beds_available`, `hospital_id`) VALUES
(5, 'General Bed', '1600.00', 'general', 77, 5),
(4, 'Pediatric Bed', '10000.00', 'bed1', 19, 5),
(6, 'Pediatric Bed', '9000.00', 'beds', 64, 6),
(8, 'General Bed', '9000.00', 'brd', 122, 9),
(9, 'Pediatric Bed', '1400.00', 'bed', 123, 11);

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_diagnosticservice`
--

DROP TABLE IF EXISTS `hospitalapp_diagnosticservice`;
CREATE TABLE IF NOT EXISTS `hospitalapp_diagnosticservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `diagnostic_service` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `service_details` longtext NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_diagnosticservice_hospital_id_7bda9cf4` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_diagnosticservice`
--

INSERT INTO `hospitalapp_diagnosticservice` (`id`, `diagnostic_service`, `price`, `service_details`, `hospital_id`) VALUES
(6, 'Endoscopy', '12000.00', 'surgery', 9),
(3, 'Endoscopy', '1222.00', 'endo scoping', 5),
(7, 'Pathology', '4533.00', 'services', 11);

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_doctoravailability`
--

DROP TABLE IF EXISTS `hospitalapp_doctoravailability`;
CREATE TABLE IF NOT EXISTS `hospitalapp_doctoravailability` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doctor_name` varchar(100) NOT NULL,
  `specialization` varchar(50) NOT NULL,
  `available_days` varchar(100) NOT NULL,
  `timings` varchar(100) NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_doctoravailability_hospital_id_4f17f1d9` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_doctoravailability`
--

INSERT INTO `hospitalapp_doctoravailability` (`id`, `doctor_name`, `specialization`, `available_days`, `timings`, `hospital_id`) VALUES
(8, 'vijay prasad', 'Cardiologist', 'Wednesday,Thursday,Friday', 'Afternoon (1:00 PM - 9:00 PM)', 9),
(9, 'rahul', 'Dermatologist', 'Thursday,Friday,Saturday', 'Morning (9:00 AM - 5:00 PM)', 11);

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_emergencyservice`
--

DROP TABLE IF EXISTS `hospitalapp_emergencyservice`;
CREATE TABLE IF NOT EXISTS `hospitalapp_emergencyservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emergency_service` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `service_details` longtext NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_emergencyservice_hospital_id_41debd25` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_emergencyservice`
--

INSERT INTO `hospitalapp_emergencyservice` (`id`, `emergency_service`, `price`, `service_details`, `hospital_id`) VALUES
(3, 'Infectious Disease Emergencies', '34000.00', 'endo scoping', 6),
(5, 'Neurological Emergencies', '2.00', '2', 8),
(6, 'Pediatric Emergencies', '3455.00', 'services', 11);

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_hospital`
--

DROP TABLE IF EXISTS `hospitalapp_hospital`;
CREATE TABLE IF NOT EXISTS `hospitalapp_hospital` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hospital_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `hospital_type` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `hospital_image` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `otp` varchar(6) NOT NULL,
  `otp_status` varchar(15) NOT NULL,
  `admin_status` varchar(15) NOT NULL,
  `hospital_doc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_hospital`
--

INSERT INTO `hospitalapp_hospital` (`id`, `hospital_name`, `email`, `contact_number`, `hospital_type`, `password`, `hospital_image`, `address`, `otp`, `otp_status`, `admin_status`, `hospital_doc`) VALUES
(8, 'newhospital', 'upenderimp25@gmail.com', '9666473716', 'Community Hospital', '1', 'hospital_images/m1_PxxcO1y_EmsaKhC_KGTQcHa.avif', '\r\nlb nagar', '6925', 'verified', 'accepted', 'hospital_document_images/m11_TuYWsQf.png'),
(11, 'newhospital2', 'team.codebook@gmail.com', '9900909099', 'Specialty Hospital', '1', 'hospital_images/apple-touch-icon.png', 'near lb nagar metro', '2572', 'verified', 'accepted', 'hospital_document_images/m6.jpg'),
(10, 'kamineni ', 'kaminani@gmail.com', '09666473716', 'Specialty Hospital', '1', 'hospital_images/m1_PxxcO1y_EmsaKhC_KGTQcHa_ne5bVQL.avif', 'lb nagar\r\nlb nagar', '6876', 'verified', 'accepted', 'hospital_document_images/m1_PxxcO1y_EmsaKhC_DcPTTL2.avif'),
(9, 'yeshoda hospital', 'yeshodahospital@gmail.com', '123456789', 'Specialty Hospital', '1', 'hospital_images/resized_ai6RcJW.jpg', 'kothapet', '8035', 'verified', 'accepted', 'hospital_document_images/m4.png');

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_medicine`
--

DROP TABLE IF EXISTS `hospitalapp_medicine`;
CREATE TABLE IF NOT EXISTS `hospitalapp_medicine` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(100) NOT NULL,
  `medicine_type` varchar(50) NOT NULL,
  `medicine_price` varchar(100) NOT NULL,
  `medicine_description` longtext NOT NULL,
  `stock_size` int NOT NULL,
  `medicine_image` varchar(100) NOT NULL,
  `hospital_id` bigint NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_medicine_hospital_id_ab8524e2` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_medicine`
--

INSERT INTO `hospitalapp_medicine` (`id`, `medicine_name`, `medicine_type`, `medicine_price`, `medicine_description`, `stock_size`, `medicine_image`, `hospital_id`, `date`) VALUES
(40, 'Dolo 650', 'Tablet', '4', 'fever', 0, 'medicine_images/d12_jY6tcif_GadoWNX.jpg', 9, '2024-02-11'),
(41, 'aspirin', 'Capsule', '21', 'painkiller', 29, 'medicine_images/apple-touch-icon.png', 11, '2024-02-11'),
(42, 'dolo 650', 'Tablet', '23', 'fever', 28, 'medicine_images/product-3.jpg', 11, '2024-02-11');

-- --------------------------------------------------------

--
-- Table structure for table `hospitalapp_surgicalservice`
--

DROP TABLE IF EXISTS `hospitalapp_surgicalservice`;
CREATE TABLE IF NOT EXISTS `hospitalapp_surgicalservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `surgical_service` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `service_details` longtext NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hospitalapp_surgicalservice_hospital_id_120f4346` (`hospital_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hospitalapp_surgicalservice`
--

INSERT INTO `hospitalapp_surgicalservice` (`id`, `surgical_service`, `price`, `service_details`, `hospital_id`) VALUES
(9, 'General Surgery', '33.00', 'new services', 9),
(8, 'General Surgery', '1.00', '1', 8),
(10, 'General Surgery', '12000.00', 'services', 11);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_appointment`
--

DROP TABLE IF EXISTS `userapp_appointment`;
CREATE TABLE IF NOT EXISTS `userapp_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `appointment_for` varchar(10) NOT NULL,
  `service_required` varchar(100) NOT NULL,
  `appointment_type` varchar(20) NOT NULL,
  `emergency_contact` varchar(15) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `hospital` varchar(100) NOT NULL,
  `user_id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_appointment_user_id_b1d8bd26` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userapp_appointment`
--

INSERT INTO `userapp_appointment` (`id`, `appointment_for`, `service_required`, `appointment_type`, `emergency_contact`, `date`, `time`, `hospital`, `user_id`, `name`, `status`) VALUES
(19, 'self', 'Regular', 'Regular', '09666473716', '2024-02-11', '16:29:19.596268', 'Hospital object (9)', 1, 'Upender', 'pending'),
(18, 'self', 'Regular', 'Regular', '09666473716', '2024-02-11', '01:12:42.922126', 'Hospital object (6)', 1, 'Upender', 'pending'),
(17, 'self', 'Regular', 'Regular', '09666473716', '2024-02-11', '01:10:58.643776', 'omini', 1, 'Upender', 'pending'),
(15, 'self', 'Consultation', 'Emergency', '9666473716', '2024-02-21', '12:12:00.000000', 'vijaya hospital', 1, 'false', 'accepted'),
(16, 'self', 'Regular', 'Regular', '09666473716', '2024-02-11', '01:07:01.374168', 'omini', 1, 'Upender', 'pending'),
(20, 'self', 'Op', 'Emergency', '9666473716', '2322-02-23', '23:23:00.000000', 'yeshoda hospital', 1, 'uppi', 'accepted'),
(21, 'self', 'Regular', 'Regular', '878765454', '2024-02-11', '17:01:28.173598', 'Hospital object (11)', 4, 'user', 'pending'),
(22, 'others', 'Surgery', 'Regular', '23431', '0412-03-12', '12:41:00.000000', 'newhospital2', 4, 'user', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_cartitem`
--

DROP TABLE IF EXISTS `userapp_cartitem`;
CREATE TABLE IF NOT EXISTS `userapp_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int UNSIGNED NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `medicine_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `status` varchar(10) NOT NULL,
  `hospital_status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_cartitem_medicine_id_9ec3511b` (`medicine_id`),
  KEY `userapp_cartitem_user_id_10d907ac` (`user_id`)
) ;

--
-- Dumping data for table `userapp_cartitem`
--

INSERT INTO `userapp_cartitem` (`id`, `quantity`, `added_at`, `medicine_id`, `user_id`, `status`, `hospital_status`) VALUES
(21, 1, '2024-02-11 11:30:41.984435', 41, 4, 'ordered', 'delivered'),
(20, 1, '2024-02-11 11:30:02.743116', 42, 4, 'ordered', 'delivered'),
(16, 1, '2024-02-11 09:37:17.359862', 40, 3, 'ordered', 'delivered'),
(18, 1, '2024-02-11 11:02:40.707666', 40, 1, 'ordered', 'pending'),
(22, 1, '2024-02-11 11:34:43.083795', 42, 4, 'pending', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_hospitalreport`
--

DROP TABLE IF EXISTS `userapp_hospitalreport`;
CREATE TABLE IF NOT EXISTS `userapp_hospitalreport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `appointment_date` date DEFAULT NULL,
  `cancellation_reason_given` tinyint(1) NOT NULL,
  `cancellation_inform` tinyint(1) NOT NULL,
  `unethical_staff_name` varchar(100) NOT NULL,
  `bill_upload` varchar(100) DEFAULT NULL,
  `medicine_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_hospitalreport_medicine_id_7ca576a8` (`medicine_id`),
  KEY `userapp_hospitalreport_user_id_60bd1d58` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `userapp_pendingmedicine`
--

DROP TABLE IF EXISTS `userapp_pendingmedicine`;
CREATE TABLE IF NOT EXISTS `userapp_pendingmedicine` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `medicine_ids` longtext NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userapp_pendingmedicine_user_id_f6f1b646` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `userapp_user`
--

DROP TABLE IF EXISTS `userapp_user`;
CREATE TABLE IF NOT EXISTS `userapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `allergies` longtext NOT NULL DEFAULT (_utf8mb3''),
  `blood_group` varchar(10) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `emergency_contact` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `relation_with_user` varchar(100) DEFAULT NULL,
  `weight` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userapp_user`
--

INSERT INTO `userapp_user` (`id`, `full_name`, `email`, `phone`, `password`, `address`, `profile_picture`, `status`, `allergies`, `blood_group`, `date_of_birth`, `emergency_contact`, `gender`, `height`, `relation_with_user`, `weight`) VALUES
(1, 'Upender', 'upenderbala25@gmail.com', '09666473716', '1', 'lb nagar', 'profile_pictures/m11_TuYWsQf.png', 'accepted', 'nothing', 'B-', '2002-01-25', '9010124374', 'male', '156cm', 'son', '40'),
(3, 'sai ', 'sai@gmail.com', '987654', '1', '09876543', 'profile_pictures/PHOTO.jpeg', 'accepted', '', '', NULL, 'None', NULL, '78cm', 'None', ''),
(4, 'user', 'newuser@gmail.com', '878765454', '1', 'lb nagar', 'profile_pictures/messages-2.jpg', 'accepted', 'cough', '', NULL, '786765756', 'female', '156cm', 'None', '56kg');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_user_medicines`
--

DROP TABLE IF EXISTS `userapp_user_medicines`;
CREATE TABLE IF NOT EXISTS `userapp_user_medicines` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `medicine_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userapp_user_medicines_user_id_medicine_id_c401ebbf_uniq` (`user_id`,`medicine_id`),
  KEY `userapp_user_medicines_user_id_af8fd7ba` (`user_id`),
  KEY `userapp_user_medicines_medicine_id_af38174f` (`medicine_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
