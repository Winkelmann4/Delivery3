
CREATE DATABASE IF NOT EXISTS Delivery5;

USE Delivery5;

CREATE TABLE IF NOT EXISTS `Kundedata` (
	`Kunde_id` INT NOT NULL AUTO_INCREMENT UNIQUE,
    `Fornavn` VARCHAR(60) NOT NULL,
    `Efternavn` VARCHAR(60) NOT NULL,
    `Email` VARCHAR(80) NOT NULL,
    PRIMARY KEY(`Kunde_id`)
    );
