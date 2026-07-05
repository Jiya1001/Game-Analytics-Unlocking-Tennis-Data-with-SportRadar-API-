-- 1. List all competitions with category names
SELECT
c.competition_name,
cat.category_name
FROM Competitions c
JOIN Categories cat
ON c.category_id = cat.category_id;

-- 2. Count competitions in each category
SELECT
cat.category_name,
COUNT(c.competition_id) AS Total_Competitions
FROM Categories cat
LEFT JOIN Competitions c
ON cat.category_id = c.category_id
GROUP BY cat.category_name;

-- 3. Find all Doubles competitions
SELECT *
FROM Competitions
WHERE type='Doubles';

-- 4. Get competitions in ATP Men category
SELECT competition_name
FROM Competitions
WHERE category_id='CAT001';

-- 5. Parent competitions
SELECT
competition_name,
parent_id
FROM Competitions;

-- 6. Competition types by category
SELECT
cat.category_name,
c.type,
COUNT(*) AS Total
FROM Competitions c
JOIN Categories cat
ON c.category_id=cat.category_id
GROUP BY cat.category_name,c.type;

-- 7. Top-level competitions
SELECT *
FROM Competitions
WHERE parent_id='';

-- 8. Venues with Complex Names
SELECT
v.venue_name,
c.complex_name
FROM Venues v
JOIN Complexes c
ON v.complex_id=c.complex_id;

-- 9. Number of venues in each complex
SELECT
complex_id,
COUNT(*) AS Total
FROM Venues
GROUP BY complex_id;

-- 10. Venues in Australia
SELECT *
FROM Venues
WHERE country_name='Australia';

-- 11. Venue Timezones
SELECT
venue_name,
timezone
FROM Venues;

-- 12. Complexes with multiple venues
SELECT
complex_id,
COUNT(*) AS Total
FROM Venues
GROUP BY complex_id
HAVING COUNT(*)>1;

-- 13. Venues grouped by country
SELECT
country_name,
COUNT(*) AS Total
FROM Venues
GROUP BY country_name;

-- 14. Competitor Rankings
SELECT
c.competitor_name,
r.rank,
r.points
FROM Competitors c
JOIN Competitor_Rankings r
ON c.competitor_id=r.competitor_id;

-- 15. Top 5 Players
SELECT
c.competitor_name,
r.rank
FROM Competitors c
JOIN Competitor_Rankings r
ON c.competitor_id=r.competitor_id
ORDER BY rank
LIMIT 5;

-- 16. Stable Rankings
SELECT
c.competitor_name,
r.rank
FROM Competitors c
JOIN Competitor_Rankings r
ON c.competitor_id=r.competitor_id
WHERE movement=0;

-- 17. Highest Points
SELECT
c.competitor_name,
MAX(points)
FROM Competitors c
JOIN Competitor_Rankings r
ON c.competitor_id=r.competitor_id;

-- 18. Competitors by Country
SELECT
country,
COUNT(*) AS Total
FROM Competitors
GROUP BY country;

-- 19. Average Points
SELECT
AVG(points)
FROM Competitor_Rankings;

-- 20. Total Competitions Played
SELECT
SUM(competitions_played)
FROM Competitor_Rankings;