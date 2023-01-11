student= {
    "name": "Krystian",
    "surname": "Paryła",
    "age": 21,
    "hobby": ["music","fashion"],
    "phone number": {"mobile":12373122,"work":562378138}    
}
import json
file= open("student.json","w",encoding="UTF-8")
json.dump(student,file,ensure_ascii=False)
file.close()