SELECT students.id, students.fullname as student_name, groups.name as group_name 
FROM students
INNER JOIN groups ON students.group_id = groups.id 
WHERE students.group_id =1
