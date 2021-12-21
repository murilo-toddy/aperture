-- Limpeza do sistema
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


-- Tabela de Notas
CREATE TABLE grade (
    subject     VARCHAR(10)     NOT NULL,
    grade       FLOAT           NOT NULL,
    CONSTRAINT pk_grade PRIMARY KEY (subject)
);


-- Inserção de disciplinas base
INSERT INTO grade (subject, grade) VALUES ('Português',   0);
INSERT INTO grade (subject, grade) VALUES ('Matemática',  0);
INSERT INTO grade (subject, grade) VALUES ('História',    0);
INSERT INTO grade (subject, grade) VALUES ('Geografia',   0);
INSERT INTO grade (subject, grade) VALUES ('Biologia',    0);
INSERT INTO grade (subject, grade) VALUES ('Física',      0);
INSERT INTO grade (subject, grade) VALUES ('Química',     0);
