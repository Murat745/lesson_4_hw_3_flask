CREATE TABLE tracks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    len_track INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(id)
);


CREATE TABLE genre(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);