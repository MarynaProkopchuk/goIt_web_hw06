SELECT subjects.id, subjects.name, teachers.fullname 
FROM subjects 
INNER JOIN teachers on subjects.teacher_id = teachers.id
WHERE subjects.teacher_id =1 


