import csv
from cs50 import SQL

artist = set()
genre = set()

open("soul2.db","w").close()

db = SQL("sqlite:///soul2.db")

db.execute("""
CREATE TABLE artist(
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_name TEXT
)
""")

db.execute("""
CREATE TABLE genre(
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name TEXT
)
""")


db.execute("""
CREATE TABLE Songs(
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year INTEGER,
    energy INTEGER,
    danceability INTEGER,
    liveness INTEGER,
    length INTEGER,
    popularity INTEGER,
    genres_id INTEGER,
    artists_id INTEGER,
    FOREIGN KEY (genres_id) REFERENCES genre(genre_id),
    FOREIGN KEY (artists_id) REFERENCES artist(artist_id)
)
""")

with open("songs.csv","r") as file:
    readers = csv.DictReader(file)

    for row in readers:
        artists_names = row["artist"]
        songs_genres = row["top genre"]

        artist.add(artists_names)
        genre.add(songs_genres)

    for line in artist:
        db.execute("INSERT INTO artist(artist_name) VALUES(?)", line)

    for line in genre:
        db.execute("INSERT INTO genre(genre_name) VALUES(?)", line)


with open("songs.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        artists_names = row["artist"]
        songs_genres = row["top genre"]
        song_titles = row["title"]
        songs_year = row["year"]
        songs_energy = row["energy"]
        songs_danceability = row["danceability"]
        songs_liveness = row["liveness"]
        songs_length = row["length"]
        songs_popularity = row["popularity"]

        db.execute("INSERT INTO Songs(title,year,energy,danceability,liveness,length,popularity,genres_id,artists_id) VALUES(?,?,?,?,?,?,?,(SELECT genre_id FROM genre WHERE genre_name = ?),(SELECT artist_id FROM artist WHERE artist_name = ?))",song_titles,songs_year,songs_energy,songs_danceability,songs_liveness,songs_length,songs_popularity,songs_genres,artists_names)
        
