-- task 17
-- ist all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g JOIN tv_show_genres AS sg ON g.id = sg.genre_id
WHERE g.id NOT IN (SELECT sg.genre_id FROM tv_shows AS s JOIN
      tv_show_genres AS sg ON s.id = sg.show_id WHERE s.title = 'Dexter')
GROUP BY g.name
ORDER BY g.name ASC;
