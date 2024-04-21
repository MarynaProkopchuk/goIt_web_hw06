SELECT 
    ROUND(AVG(grades.grade), 2) AS total_average_grade
FROM grades
ORDER BY total_average_grade DESC
LIMIT 1;

