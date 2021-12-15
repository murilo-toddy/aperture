DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


CREATE TABLE user_info (
    name        VARCHAR(20)     NOT NULL,
    surname     VARCHAR(20)     NOT NULL,
    birthday    DATE            NOT NULL
);