-- script to link genre to SUM of works related to it
USE hbtn_0d_tvshows;
SELECT tv_genres.name,
COUNT(tv_genres.id)
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY COUNT(tv_genres.id) DESC;
