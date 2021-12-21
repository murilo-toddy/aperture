DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- Tabela de informações pessoais
CREATE TABLE user_info (
    name        VARCHAR(20)     NOT NULL,
    surname     VARCHAR(20)     NOT NULL,
    birthday    DATE            NOT NULL
);


-- Tabela com tarefas da ToDoList
CREATE TABLE tasks (
    name        VARCHAR(30)     NOT NULL,
    CONSTRAINT pk_task PRIMARY KEY (name)
);


-- Tabela de disciplinas
CREATE TABLE subject (
    name        VARCHAR(10)     NOT NULL,
    CONSTRAINT pk_subject PRIMARY KEY (name)
);

-- Tabela de Notas
CREATE TABLE grade (
    subject     VARCHAR(10)     NOT NULL,
    grade       FLOAT           NOT NULL,

    CONSTRAINT pk_grade PRIMARY KEY (subject),
    CONSTRAINT fk_grade FOREIGN KEY (subject)
                REFERENCES subject (name)
                ON DELETE CASCADE
);


-- Inserção de disciplinas base
INSERT INTO subject (name) VALUES ('Português');
INSERT INTO subject (name) VALUES ('Matemática');
INSERT INTO subject (name) VALUES ('História');
INSERT INTO subject (name) VALUES ('Geografia');
INSERT INTO subject (name) VALUES ('Biologia');
INSERT INTO subject (name) VALUES ('Física');
INSERT INTO subject (name) VALUES ('Química');
