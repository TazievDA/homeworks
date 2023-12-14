INSERT INTO artist(name)
VALUES ('Metallica');

INSERT INTO artist(name)
VALUES ('Slipknot');

INSERT INTO artist(name)
VALUES ('Taylor Swift');

INSERT INTO artist(name)
VALUES ('Lo-Fi Girl');

INSERT INTO genre(name)
VALUES ('Metal');

INSERT INTO genre(name)
VALUES ('Metal');

INSERT INTO genre(name)
VALUES ('Lo-Fi');

INSERT INTO album(name, publish_date)
VALUES ('Metallica', '1991-08-12');

INSERT INTO album(name, publish_date)
VALUES ('All Hope Is Gone', '2008-08-26');

INSERT INTO album(name, publish_date)
VALUES ('Reputation', '2019-11-10');

INSERT INTO album(name, publish_date)
VALUES ('Lo-Fi mix', '2020-07-14');

INSERT INTO track(name, duration, album_id)
VALUES ('Enter Sandman', '330', 1);

INSERT INTO track(name, duration, album_id)
VALUES ('Nothing Else Matters', '387', 1);

INSERT INTO track(name, duration, album_id)
VALUES ('Psychosocial', '284', 2);

INSERT INTO track(name, duration, album_id)
VALUES ('End Game', '244', 3);

INSERT INTO track(name, duration, album_id)
VALUES ('Look What You Made Me Do', '211', 3);

INSERT INTO track(name, duration, album_id)
VALUES ('Loosing My Religion (lo-fi mix)', '235', 4);

INSERT INTO collection(name, publish_date)
VALUES ('Metall+Pop', '2023-10-11');

INSERT INTO collection(name, publish_date)
VALUES ('Only Metall', '2019-02-24');

INSERT INTO collection(name, publish_date)
VALUES ('Pop+Lo-Fi', '2018-04-02');

INSERT INTO collection(name, publish_date)
VALUES ('Top Tracks of the Year', '2023-12-30');

INSERT INTO artistgenre(artist_id, genre_id)
VALUES (1, 1);

INSERT INTO artistgenre(artist_id, genre_id)
VALUES (2, 1);

INSERT INTO artistgenre(artist_id, genre_id)
VALUES (3, 2);

INSERT INTO artistgenre(artist_id, genre_id)
VALUES (4, 3);

INSERT INTO artistalbum(artist_id, album_id)
VALUES (1, 1);

INSERT INTO artistalbum(artist_id, album_id)
VALUES (2, 2);

INSERT INTO artistalbum(artist_id, album_id)
VALUES (3, 3);

INSERT INTO artistalbum(artist_id, album_id)
VALUES (4, 4);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (1, 1);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (1, 2);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (1, 3);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (1, 4);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (2, 1);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (2, 2);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (2, 3);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (3, 4);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (3, 6);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (4, 2);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (4, 4);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (4, 6);

INSERT INTO collectiontrack(collection_id, track_id)
VALUES (4, 5);