CREATE ROLE sw_user WITH PASSWORD 'sample';
CREATE DATABASE users;
\c users;

CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE IF NOT EXISTS courses (
    id      INT PRIMARY KEY,
    name    VARCHAR(64),
    code    VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS users (
    id      INT PRIMARY KEY,
    name    VARCHAR(64) NOT NULL,
    email   VARCHAR(64) NOT NULL UNIQUE,
    status  BOOLEAN
);

CREATE TABLE IF NOT EXISTS user_courses (
    id          INT PRIMARY KEY,
    user_id     INT REFERENCES users (id),
    course_id   INT REFERENCES courses (id)
);

CREATE OR REPLACE FUNCTION getAllUsers() RETURNS SETOF users AS
$$
SELECT * FROM USERS;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION searchUsersByName(uname text) RETURNS SETOF users AS
$$
SELECT * FROM USERS WHERE name % uname;
$$
LANGUAGE 'sql';

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO sw_user;
