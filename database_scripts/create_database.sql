DROP ROLE sw_user;
DROP DATABASE users;

CREATE ROLE sw_user WITH PASSWORD 'sample' LOGIN;
CREATE DATABASE users WITH OWNER sw_user;

\c users;

CREATE EXTENSION IF NOT EXISTS pg_trgm;

DROP FUNCTION getAllUsers();
DROP FUNCTION searchUsersByName(text);
DROP FUNCTION addUser(varchar, varchar, boolean, varchar, varchar);

DROP TABLE user_courses CASCADE;
DROP TABLE courses CASCADE;
DROP TABLE users CASCADE;

CREATE TABLE courses (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(64),
    code    VARCHAR(10)
);

CREATE TABLE users (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(64) NOT NULL,
    email   VARCHAR(64) NOT NULL UNIQUE,
    phone   VARCHAR(15),
    mobile  VARCHAR(15),
    status  BOOLEAN
);

CREATE TABLE user_courses (
    id          SERIAL PRIMARY KEY,
    user_id     INT REFERENCES users (id),
    course_id   INT REFERENCES courses (id)
);

CREATE OR REPLACE FUNCTION getAllUsers() RETURNS SETOF users AS
$$
SELECT * FROM users;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION searchUsersByName(_name text) RETURNS SETOF users AS
$$
SELECT * FROM users WHERE name % _name;
$$
LANGUAGE 'sql';

CREATE OR REPLACE FUNCTION addUser(
      _name varchar, _email varchar, _status boolean, _phone varchar, _mobile varchar)
  RETURNS void AS
$$
INSERT INTO users (name, email, status, phone, mobile) VALUES
    (_name, _email, _status, _phone, _mobile);
$$
LANGUAGE 'sql';

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sw_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO sw_user;
