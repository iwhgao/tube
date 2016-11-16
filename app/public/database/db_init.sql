USE `tube`;

CREATE TABLE IF NOT EXISTS `tube_user`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `group_id`  BIGINT  COMMENT '',
  `user_id` VARCHAR(64)  COMMENT '',
  `user_name` VARCHAR(64)  COMMENT '',
  `password`  VARCHAR(64) COMMENT '',
  `email`  VARCHAR(100) COMMENT '',
  `create_time` DATETIME  COMMENT '',
  `login_time`  DATETIME  COMMENT '',
  `last_login_time`  DATETIME  COMMENT '',
  `login_times` BIGINT  COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_role`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `role_name`  VARCHAR(64)  COMMENT '',
  `role_description`  VARCHAR(200)  COMMENT '',
  `create_time` DATETIME  COMMENT ''
);



CREATE TABLE IF NOT EXISTS `tube_group`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `parent_group_id`  BIGINT COMMENT '',
  `group_name`  VARCHAR(64)  COMMENT '',
  `group_description`  VARCHAR(200)  COMMENT '',
  `create_time` DATETIME  COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_right`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `right_name`  VARCHAR(64) COMMENT '',
  `right_description` VARCHAR(200)  COMMENT '',
  `create_time` DATETIME  COMMENT  ''
);


CREATE TABLE IF NOT EXISTS `tube_role_right`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `role_id` BIGINT  COMMENT '',
  `right_id`  BIGINT  COMMENT '',
  `status`  INT COMMENT ''
);


CREATE TABLE IF NOT EXISTS `tube_group_right`(
  `id`  BIGINT  NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '',
  `group_id`  BIGINT  COMMENT '',
  `right_id`  BIGINT  COMMENT '',
  `status`  INT COMMENT ''
);