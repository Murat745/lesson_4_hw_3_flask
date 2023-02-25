CREATE TABLE tracks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist VARCHAR(50)
    title VARCHAR(100),
    genre_id INTEGER NOT NULL,
    length INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genre(id)
);

CREATE TABLE genre(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100)
);
