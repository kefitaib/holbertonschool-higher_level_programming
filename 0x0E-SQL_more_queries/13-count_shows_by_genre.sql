-- task 13
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id WHERE sg.genre_id IS NOT NULL
GROUP BY g.name
ORDER BY number_of_shows DESC;
