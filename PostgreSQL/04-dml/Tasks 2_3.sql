SELECT name, duration FROM track
WHERE duration = (SELECT max(duration) FROM track);

SELECT name FROM track
WHERE duration >= 3.5*60;

SELECT name FROM collection
WHERE publish_date BETWEEN '2017-12-31' AND '2020-12-31';

SELECT name FROM artist
WHERE name NOT LIKE '% %';

SELECT name FROM track
WHERE name LIKE '% My %';

SELECT count(artist_id), genre_id FROM artistgenre
GROUP BY genre_id;

SELECT a.name album_name, count(t.name) count_of_tracks FROM track t
JOIN album a ON t.album_id = a.album_id
GROUP BY a.publish_date, a.name
HAVING a.publish_date BETWEEN '2018-12-31' AND '2021-01-01';

SELECT a.name album_name, AVG(t.duration) FROM track t
JOIN album a ON a.album_id = t.album_id
GROUP BY album_name;

SELECT art.name artist_name FROM artist art
JOIN artistalbum ar_al ON art.artist_id = ar_al.artist_id
JOIN album a ON a.album_id = ar_al.album_id
WHERE a.publish_date NOT BETWEEN '2019-12-31' AND '2021-01-01';

SELECT DISTINCT c.name FROM collection c
JOIN collectiontrack ct ON c.collection_id = ct.collection_id
JOIN track t ON ct.track_id = t.track_id
JOIN album a ON t.album_id = a.album_id
JOIN artistalbum aa ON a.album_id = aa.album_id
JOIN artist art ON art.artist_id = aa.artist_id
WHERE art.name = 'Metallica';