CREATE DATABASE  IF NOT EXISTS `sitag` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sitag`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sitag
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Empleados');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (14,1,25),(15,1,26),(16,1,28),(17,1,29),(18,1,30),(1,1,32),(2,1,33),(3,1,34),(4,1,36),(5,1,37),(6,1,38),(7,1,40),(8,1,41),(9,1,42),(10,1,44),(11,1,45),(12,1,46),(13,1,48);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_usuario'),(22,'Can change user',6,'change_usuario'),(23,'Can delete user',6,'delete_usuario'),(24,'Can view user',6,'view_usuario'),(25,'Can add organizacion',7,'add_organizacion'),(26,'Can change organizacion',7,'change_organizacion'),(27,'Can delete organizacion',7,'delete_organizacion'),(28,'Can view organizacion',7,'view_organizacion'),(29,'Can add cliente',8,'add_cliente'),(30,'Can change cliente',8,'change_cliente'),(31,'Can delete cliente',8,'delete_cliente'),(32,'Can view cliente',8,'view_cliente'),(33,'Can add plano',9,'add_plano'),(34,'Can change plano',9,'change_plano'),(35,'Can delete plano',9,'delete_plano'),(36,'Can view plano',9,'view_plano'),(37,'Can add ubicacion',10,'add_ubicacion'),(38,'Can change ubicacion',10,'change_ubicacion'),(39,'Can delete ubicacion',10,'delete_ubicacion'),(40,'Can view ubicacion',10,'view_ubicacion'),(41,'Can add cuenta',11,'add_cuenta'),(42,'Can change cuenta',11,'change_cuenta'),(43,'Can delete cuenta',11,'delete_cuenta'),(44,'Can view cuenta',11,'view_cuenta'),(45,'Can add trabajo',12,'add_trabajo'),(46,'Can change trabajo',12,'change_trabajo'),(47,'Can delete trabajo',12,'delete_trabajo'),(48,'Can view trabajo',12,'view_trabajo'),(49,'Can add factura trabajo',13,'add_facturatrabajo'),(50,'Can change factura trabajo',13,'change_facturatrabajo'),(51,'Can delete factura trabajo',13,'delete_facturatrabajo'),(52,'Can view factura trabajo',13,'view_facturatrabajo'),(53,'Can add factura',14,'add_factura'),(54,'Can change factura',14,'change_factura'),(55,'Can delete factura',14,'delete_factura'),(56,'Can view factura',14,'view_factura'),(57,'Can add pago',15,'add_pago'),(58,'Can change pago',15,'change_pago'),(59,'Can delete pago',15,'delete_pago'),(60,'Can view pago',15,'view_pago'),(61,'Can add presupuesto',16,'add_presupuesto'),(62,'Can change presupuesto',16,'change_presupuesto'),(63,'Can delete presupuesto',16,'delete_presupuesto'),(64,'Can view presupuesto',16,'view_presupuesto');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes_cliente`
--

DROP TABLE IF EXISTS `clientes_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes_cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_cliente` varchar(10) DEFAULT 'fisica',
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `razon_social` varchar(150) DEFAULT NULL,
  `cuil` varchar(13) DEFAULT NULL,
  `telefono` varchar(14) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `localidad` varchar(40) DEFAULT NULL,
  `provincia` varchar(5) DEFAULT NULL,
  `calle` varchar(40) DEFAULT NULL,
  `numero` varchar(4) DEFAULT NULL,
  `barrio` varchar(25) DEFAULT NULL,
  `piso` varchar(5) DEFAULT NULL,
  `departamento` varchar(35) DEFAULT NULL,
  `codigo_postal` varchar(4) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes_cliente`
--

LOCK TABLES `clientes_cliente` WRITE;
/*!40000 ALTER TABLE `clientes_cliente` DISABLE KEYS */;
INSERT INTO `clientes_cliente` VALUES (1,'juridica','inta','González','Funcional León','12345679000','03644459033','funcionalleon@gmail.com','General José de San Martín','Chaco','Mariana','1334','Cebtro',NULL,'Libertador General San Martín','3700',1),(2,'fisica','Malena','González',NULL,'','03644459033','malenagzz03@gmail.com','Estación General Obligado','Chaco','mariana lopez','1334','perro',NULL,'Libertad','3700',1),(3,'fisica','Malena','González',NULL,NULL,NULL,NULL,'Pcia. Roque Sáenz Peña','Chaco','Checoslovaquia','1334','gggggggg',NULL,NULL,'3700',0),(4,'fisica','Ramon Eduardo','González',NULL,NULL,NULL,NULL,'Pcia. Roque Sáenz Peña','Chaco','checoslovaquia','1334',NULL,NULL,NULL,'3700',0),(5,'fisica','Ramon Eduardo','González',NULL,NULL,NULL,NULL,'Pcia. Roque Sáenz Peña','Chaco','Checoslovaquia','1334','gggggggg',NULL,NULL,'3700',0),(6,'fisica','Sabrina','Lopez','tyd','12345679000','03644459033','lopezsabri@gmail.com','Napalpí','Chaco','Checoslovaquia','1334','y',NULL,'25 de Mayo','3700',1),(7,'juridica','Malena Soledad','González','tyd','12345679000','03644459033','malenagzz03@gmail.com','Pcia. Roque Sáenz Peña','Chaco','Checoslovaquia','1334','nuevo',NULL,NULL,'3700',0),(8,'fisica','María','Gómez',NULL,'27-44568356-1','3624-567890','maria.gomez@example.com','Resistencia','Chaco','Av. Sarmiento','1450','Centro',NULL,NULL,'3500',1),(9,'juridica',NULL,NULL,'Constructora El Norte SRL','30-71562345-9','3625-998877','contacto@elnorte.com','Presidencia Roca','Chaco','Belgrano','890','Puerto','1','Libertador General San Martín','3503',1),(10,'fisica','Carlos','Benítez',NULL,'20-32345678-4','3624-221133','cbenitez@example.com','Fontana','Chaco','España','450','Las Flores',NULL,NULL,'3514',1),(11,'fisica','Lucía','Paredes',NULL,'27-38956214-8','3624-445566','lucia.paredes@example.com','Resistencia','Chaco','Frondizi','220','Villa Don Enrique',NULL,NULL,'3500',1),(12,'juridica',NULL,NULL,'Servicios Industriales NEA SA','30-60325478-1','3625-667788','info@si-nea.com','Puerto Vilelas','Chaco','Rivadavia','760','Industrial',NULL,NULL,'3505',1),(13,'fisica','Jorge','Ramírez',NULL,'20-31223344-0','3624-112233','jorge.ramirez@example.com','Resistencia','Chaco','French','1250','Centro','2','B','3500',1),(14,'fisica','Paula','Almirón',NULL,'27-40236789-3','3624-998877','paula.almiron@example.com','Barranqueras','Chaco','Mitre','980','San Pedro Pescador',NULL,NULL,'3503',1),(15,'juridica',NULL,NULL,'Topografía Chaqueña SRL','30-55349212-5','3625-334455','contacto@topochaco.com','Resistencia','Chaco','Pellegrini','150','Microcentro','3','C','3500',1),(16,'fisica','Silvia','Cardozo',NULL,'27-35672819-7','3624-556677','silvia.cardozo@example.com','Fontana','Chaco','Salta','345','17 de Octubre',NULL,NULL,'3514',1),(17,'fisica','Héctor','Vega',NULL,'20-44789123-2','3625-889900','hector.vega@example.com','Resistencia','Chaco','Laprida','780','Santa Inés',NULL,NULL,'3500',1),(18,'fisica','José','Rodriguez',NULL,'','3644789568','josejose@gmail.com','Pcia. Roque Sáenz Peña','Chaco','Av Malvinas Argentinas','985','Centro','6','C','3700',1),(19,'fisica',NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0),(20,'fisica',NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0),(21,'fisica',NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1),(22,'fisica','Marianela','Rinaldi',NULL,'','3358976280','mar_rinaldi@gmail.com','El Pastoril','Chaco','Barrios','369','Nado',NULL,'Mayor Luis Jorge Fontana','9852',1);
/*!40000 ALTER TABLE `clientes_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuarios_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuarios_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (3,'2025-11-11 21:04:00.577755','1','admin (Empleado)',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',6,2),(4,'2025-11-12 01:02:53.019439','1','admin (Empleado)',3,'',6,2),(5,'2025-11-12 09:20:46.475184','3','admin (Administrador)',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',6,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'clientes','cliente'),(7,'clientes','organizacion'),(4,'contenttypes','contenttype'),(14,'facturacion','factura'),(13,'facturacion','facturatrabajo'),(15,'facturacion','pago'),(16,'facturacion','presupuesto'),(5,'sessions','session'),(11,'trabajos','cuenta'),(9,'trabajos','plano'),(12,'trabajos','trabajo'),(10,'trabajos','ubicacion'),(6,'usuarios','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-10-12 13:21:10.280234'),(2,'contenttypes','0002_remove_content_type_name','2025-10-12 13:21:10.565422'),(3,'auth','0001_initial','2025-10-12 13:21:11.100557'),(4,'auth','0002_alter_permission_name_max_length','2025-10-12 13:21:11.232303'),(5,'auth','0003_alter_user_email_max_length','2025-10-12 13:21:11.246863'),(6,'auth','0004_alter_user_username_opts','2025-10-12 13:21:11.263823'),(7,'auth','0005_alter_user_last_login_null','2025-10-12 13:21:11.298024'),(8,'auth','0006_require_contenttypes_0002','2025-10-12 13:21:11.308109'),(9,'auth','0007_alter_validators_add_error_messages','2025-10-12 13:21:11.345921'),(10,'auth','0008_alter_user_username_max_length','2025-10-12 13:21:11.432155'),(11,'auth','0009_alter_user_last_name_max_length','2025-10-12 13:21:11.445643'),(12,'auth','0010_alter_group_name_max_length','2025-10-12 13:21:11.490173'),(13,'auth','0011_update_proxy_permissions','2025-10-12 13:21:11.530806'),(14,'auth','0012_alter_user_first_name_max_length','2025-10-12 13:21:11.544906'),(15,'usuarios','0001_initial','2025-10-12 13:21:13.095514'),(16,'admin','0001_initial','2025-10-12 13:21:13.430609'),(17,'admin','0002_logentry_remove_auto_add','2025-10-12 13:21:13.444780'),(18,'admin','0003_logentry_add_action_flag_choices','2025-10-12 13:21:13.494909'),(20,'sessions','0001_initial','2025-10-12 13:21:13.909764'),(25,'clientes','0001_initial','2025-10-24 21:39:30.701383'),(26,'clientes','0002_rename_estado_cliente_activo_remove_cliente_apellido_and_more','2025-10-24 21:39:30.832177'),(27,'trabajos','0001_initial','2025-10-24 21:47:29.236919'),(28,'trabajos','0002_plano_archivo_trabajo_created_at_trabajo_fecha_fin_and_more','2025-10-24 21:47:35.435101'),(30,'trabajos','0003_trabajo_opciones','2025-10-24 22:49:16.293976'),(31,'clientes','0003_remove_cliente_direccion','2025-10-25 16:02:34.260363'),(32,'clientes','0004_add_telefono_field','2025-10-25 16:05:39.583792'),(33,'clientes','0005_delete_organizacion_cliente_apellido_cliente_barrio_and_more','2025-10-25 16:28:02.010536'),(34,'clientes','0003_cliente_localidad','2025-11-11 21:01:04.279581'),(35,'trabajos','0003_alter_trabajo_fecha_inicio','2025-11-11 21:01:04.360010'),(36,'usuarios','0002_usuario_activo_alter_usuario_rol','2025-11-11 21:01:04.539589'),(37,'usuarios','0003_alter_usuario_rol','2025-11-11 21:01:04.554139'),(38,'usuarios','0004_alter_usuario_rol','2025-11-12 01:06:57.852447'),(39,'clientes','0002_alter_cliente_apellido_alter_cliente_barrio_and_more','2025-11-30 23:28:26.921875'),(40,'facturacion','0001_initial','2025-11-30 23:28:27.435067'),(42,'trabajos','0002_trabajo_costo_alter_trabajo_descripcion_and_more','2025-12-01 10:03:02.846623'),(43,'trabajos','0003_remove_trabajo_costo_trabajo_costo_total','2025-12-01 10:06:08.018384'),(44,'facturacion','0002_factura_delete_facturatrabajo','2025-12-01 10:11:43.566307'),(45,'facturacion','0003_remove_factura_estado_remove_factura_monto_pagado_and_more','2025-12-01 10:11:49.152792'),(46,'facturacion','0002_rename_costo_total_factura_monto_total','2025-12-01 10:24:03.462656'),(47,'facturacion','0003_factura_monto_pagado_presupuesto','2025-12-01 11:43:11.753715'),(48,'facturacion','0004_factura_monto_pagado','2025-12-01 11:43:55.768127'),(49,'facturacion','0005_rename_fecha_creacion_presupuesto_fecha_and_more','2025-12-01 12:43:07.447530');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('lo96bbf5h158jaqjlvtsspwkgf2h5h9s','.eJxVjEEOwiAQAP-yZ0OApQV69O4bmoVdpGrapLQn499Nkx70OjOZN4y0b3Xcm6zjxDAAwuWXJcpPmQ_BD5rvi8rLvK1TUkeiTtvUbWF5Xc_2b1CpVRhAeuoZhRMbG0qOKQXsnDgT9cFLtEXHQITIYrzzvkPRRhd22VrkAJ8v_WA4Bg:1vQ3jY:XUGRFlDm6IsszrU3A3IF6AXifkHjBs3tX39tfIkhnP0','2025-12-15 13:14:28.144977'),('lwq6xul3qnb8tscn2fywcziod463mbv9','.eJxVjDEOgzAMAP_iuYoSJ0WYsXvfgOzYKbQVSAQm1L9XSAztene6HXre1qHfqi39qNABwuWXCeeXTYfQJ0-P2eV5WpdR3JG401Z3n9Xet7P9GwxcB-iAWvRWUikavZC3JlokiUqJveqVDUnaJvhgXEQoJ9SQPRJZ4ISM8PkC9ow4Ug:1vIzTu:K1hpydCmxDNBBz5LefrS_xBrjzIrqHM7K1dCkHAJXAQ','2025-11-26 01:17:06.178640'),('on55xvai5z4vvfdu23zj2u9me3e0o9ya','.eJxVjMEOgjAQBf9lz6aBFbqFo3e-gby2W4saSCicjP9uSDjodWYybxqxb3nci67jFKmnmi6_zCM8dT5EfGC-LyYs87ZO3hyJOW0xwxL1dTvbv0FGydQTSyWKRlo0ipbR2ijxqp237DqE5JQl1F2qAestHEtqbOUQgjJLVPp8AepVOGo:1v8UNh:-V3du87bnMEao_JNHf7xVqmnhbt3r9tL9QSWdd8PAdk','2025-10-28 02:03:17.436138'),('t8ti7qce21bhotmjuzel2vx8wx6ycppm','.eJxVjMEOgjAQBf9lz6aBFbqFo3e-gby2W4saSCicjP9uSDjodWYybxqxb3nci67jFKmnmi6_zCM8dT5EfGC-LyYs87ZO3hyJOW0xwxL1dTvbv0FGydQTSyWKRlo0ipbR2ijxqp237DqE5JQl1F2qAestHEtqbOUQgjJLVPp8AepVOGo:1v86No:nsSkqX0dwrdgy1ppt5ZNGxffri6B9qHGojGUvKSSp0E','2025-10-27 00:25:48.446212'),('y8kp3nmyc7hlhzyujlevmik4409k3el0','.eJxVjEsKwjAUAK9S3jqEfNq0dulaT9CUkF9_agJNC4J4dwlU0O3MMC9Qet8mtSe_qtlBCyWgX2a0vfmQhVt0GCO2MWzrbHBO8GETvkbn7-ej_RtMOk3QQkX4QCtr-IlzdxKCGEqJJ4y5uhHWlE3DB0otJ1ZQIcSgnfFUO0JrLljNbJ4-fEp69Ala6DoJSi0phi-VgAqCClahQsIljnMo_HPeYoo4KwkS-h7eH992TNU:1vPjUM:gxaEVtmCvBIvIws4CeBhCjRD9e91z4lJnL1pfp7QTME','2025-12-14 15:37:26.110823');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturacion_factura`
--

DROP TABLE IF EXISTS `facturacion_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturacion_factura` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `monto_total` decimal(12,2) NOT NULL,
  `monto_pagado` decimal(12,2) NOT NULL,
  `saldo_pendiente` decimal(12,2) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `cliente_id` bigint NOT NULL,
  `trabajo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `trabajo_id` (`trabajo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturacion_factura`
--

LOCK TABLES `facturacion_factura` WRITE;
/*!40000 ALTER TABLE `facturacion_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturacion_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturacion_presupuesto`
--

DROP TABLE IF EXISTS `facturacion_presupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturacion_presupuesto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `observaciones` longtext NOT NULL,
  `superficie` decimal(10,2) NOT NULL,
  `costo_estimado` decimal(12,2) NOT NULL,
  `aprobado` tinyint(1) NOT NULL,
  `fecha` date NOT NULL,
  `cliente_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `facturacion_presupue_cliente_id_3aa00db7_fk_clientes_` (`cliente_id`),
  CONSTRAINT `facturacion_presupue_cliente_id_3aa00db7_fk_clientes_` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturacion_presupuesto`
--

LOCK TABLES `facturacion_presupuesto` WRITE;
/*!40000 ALTER TABLE `facturacion_presupuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturacion_presupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajos_cuenta`
--

DROP TABLE IF EXISTS `trabajos_cuenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajos_cuenta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `costo_total` decimal(12,2) NOT NULL,
  `monto_pagado` decimal(12,2) NOT NULL,
  `saldo_pendiente` decimal(12,2) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `cliente_id` bigint NOT NULL,
  `trabajo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `trabajo_id` (`trabajo_id`),
  KEY `facturacion_factura_cliente_id_a467a777_fk_clientes_cliente_id` (`cliente_id`),
  CONSTRAINT `facturacion_factura_cliente_id_a467a777_fk_clientes_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_cliente` (`id`),
  CONSTRAINT `facturacion_factura_trabajo_id_b1ae2dcb_fk_trabajos_trabajo_id` FOREIGN KEY (`trabajo_id`) REFERENCES `trabajos_trabajo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajos_cuenta`
--

LOCK TABLES `trabajos_cuenta` WRITE;
/*!40000 ALTER TABLE `trabajos_cuenta` DISABLE KEYS */;
INSERT INTO `trabajos_cuenta` VALUES (1,5000000.00,5000000.00,0.00,'pagado','2025-11-30',5,19);
/*!40000 ALTER TABLE `trabajos_cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajos_plano`
--

DROP TABLE IF EXISTS `trabajos_plano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajos_plano` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `descripcion` varchar(255) NOT NULL DEFAULT '',
  `trabajo_id` bigint NOT NULL,
  `ubicacion_id` bigint NOT NULL,
  `archivo` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `trabajos_plano_trabajo_id_38e2c783_fk_trabajos_trabajo_id` (`trabajo_id`),
  KEY `trabajos_plano_ubicacion_id_8b1f3420_fk_trabajos_ubicacion_id` (`ubicacion_id`),
  CONSTRAINT `trabajos_plano_trabajo_id_38e2c783_fk_trabajos_trabajo_id` FOREIGN KEY (`trabajo_id`) REFERENCES `trabajos_trabajo` (`id`),
  CONSTRAINT `trabajos_plano_ubicacion_id_8b1f3420_fk_trabajos_ubicacion_id` FOREIGN KEY (`ubicacion_id`) REFERENCES `trabajos_ubicacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajos_plano`
--

LOCK TABLES `trabajos_plano` WRITE;
/*!40000 ALTER TABLE `trabajos_plano` DISABLE KEYS */;
/*!40000 ALTER TABLE `trabajos_plano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajos_trabajo`
--

DROP TABLE IF EXISTS `trabajos_trabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajos_trabajo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `cliente_id` bigint NOT NULL,
  `estado` varchar(20) NOT NULL DEFAULT 'pendiente',
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `fecha_fin` date DEFAULT NULL,
  `responsable_id` bigint DEFAULT NULL,
  `titulo` varchar(250) NOT NULL DEFAULT '',
  `ubicacion_id` bigint DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `opciones` varchar(255) NOT NULL DEFAULT '',
  `costo` decimal(12,2) NOT NULL,
  `costo_total` decimal(12,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `trabajos_trabajo_cliente_id_c6ff11c4_fk_clientes_cliente_id` (`cliente_id`),
  KEY `trabajos_trabajo_responsable_id_8ee3d2c5_fk_usuarios_usuario_id` (`responsable_id`),
  KEY `trabajos_trabajo_ubicacion_id_2ff76f87_fk_trabajos_ubicacion_id` (`ubicacion_id`),
  CONSTRAINT `trabajos_trabajo_cliente_id_c6ff11c4_fk_clientes_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_cliente` (`id`),
  CONSTRAINT `trabajos_trabajo_responsable_id_8ee3d2c5_fk_usuarios_usuario_id` FOREIGN KEY (`responsable_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `trabajos_trabajo_ubicacion_id_2ff76f87_fk_trabajos_ubicacion_id` FOREIGN KEY (`ubicacion_id`) REFERENCES `trabajos_ubicacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajos_trabajo`
--

LOCK TABLES `trabajos_trabajo` WRITE;
/*!40000 ALTER TABLE `trabajos_trabajo` DISABLE KEYS */;
INSERT INTO `trabajos_trabajo` VALUES (1,'Mensura de precisión para subdivisión de parcela rural. Incluye replanteo de vértices y amojonamiento en campo.','2025-11-30',5,'Pendiente',1,'2025-10-26 16:33:43.022931',NULL,6,'Mensura Lote 12',1,'2025-11-24 14:03:08.771810','',0.00,0.00),(2,'Verificación y demarcación de límites de parcela urbana. Incluye informe técnico y plano de deslinde.','2021-01-11',11,'Finalizado',1,'2025-11-12 01:21:40.214542',NULL,2,'Deslinde de Propiedad Urbana',4,'2025-11-15 14:52:41.218571','',0.00,0.00),(15,'Mensura y subdivisión de parcela rural en 12 lotes.','2025-01-13',8,'Finalizado',1,'2025-11-15 14:46:44.381434',NULL,5,'Loteo 156-B',5,'2025-11-15 14:54:06.242738','',0.00,0.00),(16,'Estudio planialtimétrico detallado de 15 hectáreas para futura ampliación de la planta. Incluye curvas de nivel cada 0.5m.','2025-11-20',14,'Pendiente',1,'2025-11-15 14:52:24.485702',NULL,6,'Relevamiento Planialtimétrico de Predio Industrial',6,'2025-11-15 14:53:17.756011','',0.00,0.00),(17,'ssssssssssssssssssssssssssssss','2025-11-21',8,'Pendiente',1,'2025-11-30 15:55:00.440491',NULL,3,'Relevamiento topografico',7,'2025-11-30 15:55:00.440529','',0.00,0.00),(18,'bbbbbbbbbbb',NULL,2,'Pendiente',1,'2025-11-30 15:56:53.806292',NULL,2,'',8,'2025-11-30 15:56:53.806341','',0.00,0.00),(19,'5555555555555555555555','2025-11-19',18,'En curso',1,'2025-11-30 21:52:32.311066',NULL,4,'Loteo 156-B',9,'2025-11-30 21:52:32.311103','',0.00,0.00),(20,'aaaaaa','2025-11-30',1,'Pendiente',1,'2025-11-30 23:15:18.924045',NULL,3,'Deslinde de Propiedad Urbana',10,'2025-11-30 23:15:18.924083','',0.00,0.00);
/*!40000 ALTER TABLE `trabajos_trabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajos_ubicacion`
--

DROP TABLE IF EXISTS `trabajos_ubicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajos_ubicacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `numero` int NOT NULL,
  `calle` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `barrio` varchar(45) DEFAULT NULL,
  `nomenclatura_catastral` varchar(50) DEFAULT NULL,
  `departamento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajos_ubicacion`
--

LOCK TABLES `trabajos_ubicacion` WRITE;
/*!40000 ALTER TABLE `trabajos_ubicacion` DISABLE KEYS */;
INSERT INTO `trabajos_ubicacion` VALUES (1,1020,'Ruta Nacional 11','La Leonesa',NULL,'01-02-156-42',NULL),(2,1334,'Checoslovaquia','Pcia. Roque Sáenz Peña','gggggggg','ggggggggg',NULL),(3,1334,'Checoslovaquia','Pcia. Roque Sáenz Peña','gggggggg','ggggggggg',NULL),(4,1234,'Av San Martin','Resistencia','Centro','12-34-567-89',NULL),(5,785,'San Martin','Charata','-','58-09-85-369',NULL),(6,0,'Acceso Norte','Barranqueras','Parque Industrial','02-05-884-12',NULL),(7,896,'Jose Maria','Roque Sáenz Peña','Lamadrid','985632',NULL),(8,0,'0',NULL,NULL,NULL,NULL),(9,1334,'Checoslovaquia','Pcia. Roque Sáenz Peña','Parque Industrial','Circ 4 Mz 9',NULL),(10,1334,'Checoslovaquia','Pcia. Roque Sáenz Peña','Parque Industrial','985632',NULL);
/*!40000 ALTER TABLE `trabajos_ubicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario`
--

DROP TABLE IF EXISTS `usuarios_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
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
  `rol` varchar(20) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario`
--

LOCK TABLES `usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario` DISABLE KEYS */;
INSERT INTO `usuarios_usuario` VALUES (1,'pbkdf2_sha256$???$dummy',NULL,0,'mfernandez','','Fernández','marcelo.fernandez@sitag.com',1,1,'2025-01-01 08:00:00.000000','administrador',1),(2,'pbkdf2_sha256$1000000$eZOnUsQNOlTIOHeyAt9qGb$d0dhN65VXzeiCcSFuLHgSypdEXyYtUIMGaGXysByRNo=','2025-11-15 14:40:06.430048',1,'malena','','','noeliag0925@gmail.com',1,1,'2025-11-11 21:03:07.735751','administrador',1),(3,'pbkdf2_sha256$1000000$HS320jTBkfCZiPzslXsamJ$bhFcYt3yq4JClsgGgldcKO7HOcQu/UFmTTkMl1pvtzc=','2025-11-30 23:53:34.921077',0,'admin','Administrador','','administrador@gmail.com',1,1,'2025-11-12 01:17:41.000000','administrador',1),(4,'pbkdf2_sha256$1000000$1kFExIL2tup0fdhTOJvws0$3f33R1h+wH+G1x85Idb7SQcwkmfVQcQpmubWcgpSzJU=','2025-11-30 15:37:27.929966',0,'melisamelgarejo','Meli Melgarejo','','meli@gmail.com',0,1,'2025-11-12 02:01:26.426123','empleado',1),(5,'pbkdf2_sha256$???$dummy',NULL,0,'rgutierrez','','Gutiérrez','roxana.gutierrez@sitag.com',1,1,'2025-01-02 09:30:00.000000','empleado',1),(6,'pbkdf2_sha256$???$dummy',NULL,0,'dmansilla','Diego','Mansilla','diego.mansilla@sitag.com',1,1,'2025-01-03 11:15:00.000000','responsable',1),(7,'pbkdf2_sha256$1000000$QWTJk1MdMw1p0iSRp5p7P9$6IYFn/00aUFxPeH5D0Dd0ZJWz9u6ZhGD0R6rdEbC0YU=',NULL,0,'oliviarodrigo','','','oliviarodrigo@gmail.com',0,1,'2025-11-30 15:32:28.881405','administrador',1),(8,'pbkdf2_sha256$1000000$uN4TnFABXyAC91rJfbx2x2$ny+wi0kSM+ndI0iQ4eozSxvZfOfC2U0WQAl/I9woHQ0=',NULL,0,'lilmix','Little Mix','','LITTLEMIX@GMAIL.COM',0,1,'2025-11-30 15:52:30.261158','empleado',1);
/*!40000 ALTER TABLE `usuarios_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario_groups`
--

DROP TABLE IF EXISTS `usuarios_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_groups_usuario_id_group_id_4ed5b09e_uniq` (`usuario_id`,`group_id`),
  KEY `usuarios_usuario_groups_group_id_e77f6dcf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuarios_usuario_gro_usuario_id_7a34077f_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `usuarios_usuario_groups_group_id_e77f6dcf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario_groups`
--

LOCK TABLES `usuarios_usuario_groups` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuarios_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_user_pe_usuario_id_permission_id_217cadcd_uniq` (`usuario_id`,`permission_id`),
  KEY `usuarios_usuario_use_permission_id_4e5c0f2f_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuarios_usuario_use_permission_id_4e5c0f2f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuarios_usuario_use_usuario_id_60aeea80_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario_user_permissions`
--

LOCK TABLES `usuarios_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'sitag'
--

--
-- Dumping routines for database 'sitag'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-05 18:02:09
