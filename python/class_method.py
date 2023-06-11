class Student:
    # class attribue
    school_name="Leads School"

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def get_student_information(self):
        return f'Student name is:{self.name}.\nStudent age is:{self.age}.\nStudent gender is:{self.gender}'
    @classmethod
    def get_school_name(cls):
        return cls.school_name

    
person_1=Student('Zubaer', 21, 'M')
person_2=Student('Hana', 31, 'F')

print(person_1.school_name)
print(person_1.get_student_information())
print(person_2.school_name)
print(person_2.get_student_information())

print(Student.get_school_name())