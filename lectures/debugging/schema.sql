DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS
(
    id integer PRIMARY KEY,
    username string,
    CONSTRAINT constraint_name UNIQUE (username)
);

