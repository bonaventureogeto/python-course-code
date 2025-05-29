-- 1NF
CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- 2NF
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- 3NF
CREATE TABLE post_tags (
    post_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY(post_id) REFERENCES posts(post_id),
    FOREIGN KEY(tag_id) REFERENCES tags(tag_id)
);


-- 1NF, 2NF, 3NF