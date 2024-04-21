SELECT groups.name as group_name, subjects.name as subject_name,
ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
INNER JOIN subjects ON grades.subject_id  = subjects.id 
INNER JOIN students ON grades.student_id = students.id
INNER JOIN groups ON students.group_id = groups.id 
WHERE subject_id =1
GROUP BY groups.id