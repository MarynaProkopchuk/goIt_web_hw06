WITH NewTable AS
	(SELECT groups.id, groups.name as group_name, subjects.name as subject_name, grades.grade, students.fullname as student_name 
	FROM grades
	INNER JOIN subjects ON grades.subject_id  = subjects.id 
	INNER JOIN students ON grades.student_id = students.id
	INNER JOIN groups ON students.group_id = groups.id 
	WHERE subject_id =1)
SELECT
	group_name,subject_name, grade, student_name 
	FROM NewTable
	WHERE id=1
	;



