#Class is a blueprint of an object.
#Object is an instance of a class

class Student:
    #Attributes

    name = "Joy"
    age = 23
    gender = "Female"
    course = "MIT"

    #Behaviour/Functions
    def study(self):
         print("Student is studying")

student1 = Student() #Creating an object
student1.study()
print(student1.name)

student2 = Student()
student2.study()
student3 = Student()









