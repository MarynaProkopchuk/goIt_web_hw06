SELECT students.fullname as student_name, subjects.name as subject_name 
FROM subjects 
INNER JOIN grades ON grades.subject_id  = subjects.id 
INNER JOIN students ON grades.student_id = students.id
WHERE student_id = 5
GROUP BY subject_id 



