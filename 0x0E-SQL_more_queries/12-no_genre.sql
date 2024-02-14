-- Imports databaase dump from hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
WHERE genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
