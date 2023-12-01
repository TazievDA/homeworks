CREATE TABLE IF NOT EXISTS Genre(
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);
CREATE TABLE IF NOT EXISTS Artist(
	artist_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);
CREATE TABLE IF NOT EXISTS ArtistGenre(
	artist_id INTEGER REFERENCES Artist(artist_id),
	genre_id INTEGER REFERENCES Genre(genre_id)
);
CREATE TABLE IF NOT EXISTS Album(
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	publish_date DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS ArtistAlbum(
	artist_id INTEGER REFERENCES Artist(artist_id),
	album_id INTEGER REFERENCES Album(album_id)
);
CREATE TABLE IF NOT EXISTS Track(
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER REFERENCES Album(album_id)
);
CREATE TABLE IF NOT EXISTS Collection(
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	publish_date DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS CollectionTrack(
	collection_id INTEGER REFERENCES Collection(collection_id),
	track_id INTEGER REFERENCES Track(track_id)
);