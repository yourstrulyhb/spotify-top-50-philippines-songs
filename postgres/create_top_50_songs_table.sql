CREATE TABLE IF NOT EXISTS top_50_songs_ph (
	id SERIAL PRIMARY KEY,
	song_rank INT NOT NULL,
	spotify_id VARCHAR(255) NOT NULL,
	title VARCHAR(255) NOT NULL,
	artists VARCHAR(255) NOT NULL,
	date_gathered DATE NOT NULL,
	popularity INT,
	album_name VARCHAR(255),
	album_release_date DATE,
	album_spotify_id VARCHAR(255)
);
	