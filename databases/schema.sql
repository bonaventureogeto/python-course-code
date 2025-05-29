CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE
);

ALTER TABLE users ADD bio TEXT;

DROP TABLE IF EXISTS old_table

