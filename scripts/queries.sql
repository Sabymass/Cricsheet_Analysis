-- 1. Top 10 batsmen by total runs in ODI matches
SELECT batter, SUM(runs) AS total_runs
FROM matches_odis
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

-- 2. Top 10 batsmen by total runs in T20 matches
SELECT batter, SUM(runs) AS total_runs
FROM matches_t20s
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

-- 3. Top 10 batsmen by total runs in Test matches
SELECT batter, SUM(runs) AS total_runs
FROM matches_tests
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

-- 4. Leading wicket-takers in ODI matches
SELECT bowler, SUM(wicket) AS total_wickets
FROM matches_odis
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10;

-- 5. Leading wicket-takers in T20 matches
SELECT bowler, SUM(wicket) AS total_wickets
FROM matches_t20s
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10;

-- 6. Leading wicket-takers in Test matches
SELECT bowler, SUM(wicket) AS total_wickets
FROM matches_tests
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10;

-- 7. Team with highest total runs in ODI matches
SELECT batting_team, SUM(runs + extras) AS total_runs
FROM matches_odis
GROUP BY batting_team
ORDER BY total_runs DESC
LIMIT 1;

-- 8. Team with highest total runs in T20 matches
SELECT batting_team, SUM(runs + extras) AS total_runs
FROM matches_t20s
GROUP BY batting_team
ORDER BY total_runs DESC
LIMIT 1;

-- 9. Team with highest total runs in Test matches
SELECT batting_team, SUM(runs + extras) AS total_runs
FROM matches_tests
GROUP BY batting_team
ORDER BY total_runs DESC
LIMIT 1;

-- 10. Total number of centuries across ODI matches
SELECT COUNT(*) AS centuries
FROM matches_odis
WHERE runs >= 100;

-- 11. Total number of centuries across T20 matches
SELECT COUNT(*) AS centuries
FROM matches_t20s
WHERE runs >= 100;

-- 12. Total number of centuries across Test matches
SELECT COUNT(*) AS centuries
FROM matches_tests
WHERE runs >= 100;

-- 13. Matches with the narrowest margin of victory in ODI matches
SELECT match_id, ABS(SUM(runs + extras)) AS margin
FROM matches_odis
GROUP BY match_id
ORDER BY margin ASC
LIMIT 5;

-- 14. Matches with the narrowest margin of victory in T20 matches
SELECT match_id, ABS(SUM(runs + extras)) AS margin
FROM matches_t20s
GROUP BY match_id
ORDER BY margin ASC
LIMIT 5;

-- 15. Matches with the narrowest margin of victory in Test matches
SELECT match_id, ABS(SUM(runs + extras)) AS margin
FROM matches_tests
GROUP BY match_id
ORDER BY margin ASC
LIMIT 5;

-- 16. Average runs per match by top 10 batsmen in ODI
SELECT batter, SUM(runs)*1.0/COUNT(DISTINCT match_id) AS avg_runs
FROM matches_odis
GROUP BY batter
ORDER BY avg_runs DESC
LIMIT 10;

-- 17. Average runs per match by top 10 batsmen in T20
SELECT batter, SUM(runs)*1.0/COUNT(DISTINCT match_id) AS avg_runs
FROM matches_t20s
GROUP BY batter
ORDER BY avg_runs DESC
LIMIT 10;

-- 18. Average runs per match by top 10 batsmen in Test
SELECT batter, SUM(runs)*1.0/COUNT(DISTINCT match_id) AS avg_runs
FROM matches_tests
GROUP BY batter
ORDER BY avg_runs DESC
LIMIT 10;

-- 19. Total wickets by team in ODI matches
SELECT batting_team, SUM(wicket) AS total_wickets
FROM matches_odis
GROUP BY batting_team
ORDER BY total_wickets DESC;

-- 20. Total wickets by team in T20 matches
SELECT batting_team, SUM(wicket) AS total_wickets
FROM matches_t20s
GROUP BY batting_team
ORDER BY total_wickets DESC;
