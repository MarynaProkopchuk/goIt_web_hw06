WITH NewTable AS
	(SELECT subjects.name as subject, students.fullname student_name, teachers.fullname as teacher_name, teachers.id  
	FROM grades
	INNER JOIN subjects ON grades.subject_id  = subjects.id 
	INNER JOIN students ON grades.student_id = students.id
	INNER JOIN teachers  ON subjects.teacher_id = teachers.id 
	WHERE student_id  =1
	GROUP BY subject_id)
SELECT
	teacher_name,subject, student_name
	FROM NewTable
	WHERE id=1
	;
