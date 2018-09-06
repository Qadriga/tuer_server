-- BIGINT 64 bit value TINYINT 8 bit value
CREATE DATABASE IF NOT EXISTS door;
USE door;
CREATE TABLE  IF NOT EXISTS tagtype(
	tag_type TINYINT UNIQUE NOT NULL PRIMARY KEY,
	custom_description VARCHAR(120) NOT NULL);
CREATE TABLE  IF NOT EXISTS users(
    tag_id BIGINT UNIQUE NOT NULL PRIMARY KEY,
    tag_type tinyint NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    active TINYINT DEFAULT 0,
    FOREIGN KEY (tag_type) REFERENCES tagtype( tag_type)
);


CREATE TABLE  IF NOT EXISTS allowed_users(
    user_tag_id BIGINT NOT NULL,
    user_valid_start DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_valid_end DATETIME NULL DEFAULT NULL,
    FOREIGN KEY (user_tag_id) REFERENCES users(tag_id) 
);
CREATE TABLE  IF NOT EXISTS loggin(
	logtime DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP,
	door_id TINYINT NOT NULL DEFAULT -1,
	used_tag_id BIGINT DEFAULT -1,
	description VARCHAR(100)
);

