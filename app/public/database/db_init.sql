USE `tube`;

CREATE TABLE IF NOT EXISTS `tube_user`(
  `user_id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `user_name` VARCHAR(64)  NOT NULL COMMENT '',
  `group_id`  BIGINT  NOT NULL DEFAULT 0 COMMENT '',
  `password`  VARCHAR(64) NOT NULL COMMENT '',
  `email`  VARCHAR(100) DEFAULT NULL COMMENT '',
  `avatar`  VARCHAR(200) DEFAULT NULL COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT '',
  `login_time`  DATETIME  DEFAULT NULL COMMENT '',
  `last_login_time`  DATETIME  DEFAULT NULL COMMENT '',
  `login_times` BIGINT  DEFAULT 0 COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_role`(
  `role_id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `role_name`  VARCHAR(64)  NOT NULL COMMENT '',
  `role_description`  VARCHAR(200)  DEFAULT NULL COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT ''
);



CREATE TABLE IF NOT EXISTS `tube_group`(
  `group_id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `parent_group_id`  BIGINT NOT NULL COMMENT '',
  `group_name`  VARCHAR(64)  NOT NULL COMMENT '',
  `group_description`  VARCHAR(200)  DEFAULT NULL COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_right`(
  `right_id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `right_name`  VARCHAR(64) NOT NULL COMMENT '',
  `right_description` VARCHAR(200)  DEFAULT NULL COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT  ''
);


CREATE TABLE IF NOT EXISTS `tube_role_right`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `role_id` BIGINT  NOT NULL COMMENT '',
  `right_id`  BIGINT  NOT NULL COMMENT '',
  `status`  INT NOT NULL DEFAULT 0 COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_group_right`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `group_id`  BIGINT  NOT NULL COMMENT '',
  `right_id`  BIGINT  NOT NULL COMMENT '',
  `status`  INT NOT NULL DEFAULT 0 COMMENT ''
);

CREATE TABLE IF NOT EXISTS `tube_project`(
  `project_id`  BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `project_name` VARCHAR(100) NOT NULL COMMENT '',
  `project_description` VARCHAR(200) DEFAULT NULL COMMENT '',
  `user_id` BIGINT NOT NULL COMMENT '',
  `user_name` VARCHAR(64) COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT '',
  `last_update_time`  DATETIME  DEFAULT NULL COMMENT ''
);

CREATE TABLE IF NOT EXISTS `tube_project_right_code`(
  `project_right_code`  INT NOT NULL COMMENT '',
  `project_right_name`  VARCHAR(64) NOT NULL COMMENT '',
  `project_right_description` VARCHAR(100)  NOT NULL COMMENT ''
);

CREATE TABLE IF NOT EXISTS `tube_project_member`(
  `project_member_id` BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `project_id`  BIGINT NOT NULL COMMENT '',
  `user_id` BIGINT  NOT NULL COMMENT '',
  `user_name` VARCHAR(64) NOT NULL COMMENT '',
  `create_time` DATETIME  NOT NULL COMMENT '',
  `project_right_code`  VARCHAR(16) NOT NULL DEFAULT '0'  COMMENT ''
);

CREATE TABLE IF NOT EXISTS `tube_catalog`(
  `catalog_id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `catalog_name`  VARCHAR(64) NOT NULL COMMENT '',
  `project_id`  BIGINT  NOT NULL COMMENT '',
  `sort_no` INT NOT NULL DEFAULT 0  COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT '',
  `last_update_time`  DATETIME  DEFAULT NULL COMMENT '',
  `parent_catalog_id`  BIGINT  NOT NULL DEFAULT 0 COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_page`(
  `page_id` BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `creator_user_id` BIGINT  NOT NULL COMMENT '',
  `creator_user_name` VARCHAR(64) NOT NULL COMMENT '',
  `project_id`  BIGINT  NOT NULL COMMENT '',
  `catalog_id`  BIGINT  NOT NULL COMMENT '',
  `page_title`  VARCHAR(100)  NOT NULL COMMENT '',
  `page_content`  TEXT  NOT NULL COMMENT '',
  `sort_no` BIGINT  NOT NULL DEFAULT 0  COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_template`(
  `template_id` BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `user_id` BIGINT NOT NULL COMMENT '',
  `template_title`  VARCHAR(100)  NOT NULL COMMENT '',
  `template_content`  TEXT  NOT NULL COMMENT '',
  `create_time` DATETIME  DEFAULT NULL COMMENT '',
  `last_update_time`  DATETIME  DEFAULT NULL COMMENT ''
);