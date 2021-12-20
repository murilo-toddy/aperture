DROP SCHEMA public CASCADE;
CREATE SCHEMA public;


CREATE TABLE user_info (
    name        VARCHAR(20)     NOT NULL,
    surname     VARCHAR(20)     NOT NULL,
    birthday    DATE            NOT NULL
);


CREATE TABLE subject (
    name        VARCHAR(10)     NOT NULL,
    year        DATE            NOT NULL
);


CREATE TABLE grade (
    subject     VARCHAR(10)     NOT NULL,
    year        DATE            NOT NULL,
    grade       FLOAT           NOT NULL,

    CONSTRAINT pk_grade PRIMARY KEY(subject, year),
    CONSTRAINT fk_grade FOREIGN KEY(subject, year)
                REFERENCES subject(name, year)
                ON DELETE CASCADE
);