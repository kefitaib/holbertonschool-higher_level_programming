-- task 20
-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating
FROM tv_show_ratings AS r, tv_genres AS g JOIN tv_show_genres AS sg ON g.id = sg.genre_id
WHERE sg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
