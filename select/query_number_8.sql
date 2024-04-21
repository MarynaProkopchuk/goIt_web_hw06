SELECT teachers.fullname as teacher_name, subjects.name as subject, 
ROUND(AVG(grades.grade), 2) AS average_grade
	FROM grades
	INNER JOIN subjects ON grades.subject_id  = subjects.id 
	INNER JOIN students ON grades.student_id = students.id
	INNER JOIN teachers  ON subjects.teacher_id = teachers.id 
	WHERE teacher_id  =1
	GROUP BY subject_id 
