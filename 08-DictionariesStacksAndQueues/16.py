import json
file1 = open("students.json","r",encoding="UTF-8")
file2 = open("limited.json","w",encoding="UTF-8")

filecontent= json.load(file1)
for student in filecontent:
    limited_student={
        "name": student["first_name"],
        "surname": student["surname"],
        "student_id":student["student_id"]
    }
    json.dump(limited_student, file2, ensure_ascii=False)
file1.close()
file2.close()
        
    
    