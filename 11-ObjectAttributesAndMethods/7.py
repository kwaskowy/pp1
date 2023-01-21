class Student():
    last_id= 100000
    def __init__(self,name,surname,field):
        self.name= name
        self.surname= surname.upper()
        self.field= field
        Student.last_id+=1
        self.id=Student.last_id
    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}), {self.field}, UEK Kraków"

student1= Student("Krystian","Paryła","Applied Informatics")
print(student1)
print()
student2= Student("Jason","Derulo","Innovation in Business")
print(student2)
print()
student3= Student("Krzysztof","Kononowicz","Finance and Accounting")
print(student3)