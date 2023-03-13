-- development
CREATE DATABASE test DEFAULT CHARACTER SET utf8mb4;
CREATE USER 'test'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'test'@'%';
FLUSH PRIVILEGES;
use test;
CREATE TABLE stocks (
    id SERIAL UNIQUE,
    name text
);

CREATE TABLE sales (
    id SERIAL UNIQUE,
    name text,
    price int
);