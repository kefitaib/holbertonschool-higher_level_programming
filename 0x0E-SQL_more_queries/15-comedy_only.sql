-- task 15
-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_genres AS g JOIN tv_show_genres AS sg ON g.id = sg.genre_id
JOIN tv_shows AS s ON s.id = sg.show_id
WHERE g.name = 'Comedy'
GROUP BY s.title
ORDER BY s.title ASC;
