SELECT 
    students.id, 
    students.fullname, 
    ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
JOIN students  ON students.id = grades.student_id
where grades.subject_id = 3
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;