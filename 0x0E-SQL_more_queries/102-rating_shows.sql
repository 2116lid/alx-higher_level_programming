-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
SELECT `title`, SUM(`rate`) AS total FROM `tv_shows`
INNER JOIN `tv_show_ratings` ON `tv_shows`.`id` = `tv_show_ratings`.`show_id`
GROUP BY `title`
ORDER BY total DESC;
