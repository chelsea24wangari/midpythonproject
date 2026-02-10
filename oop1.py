class Employee:

    #Attributes
    def __init__(self, fullname, position, status, age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    #Behaviour/Function
    def work(self):
        print(self.fullname,"is working")

employee1 = Employee("Ken Mwenda", "MD","Married",54)
print(employee1.fullname, employee1.status, employee1.position, employee1.age)
employee1.work()

employee2 = Employee("Frank Ocean","Programme Manager","Single",34)
print(employee2.fullname, employee2.status, employee2.position, employee2.age)

employee3 = Employee("Alice Kimani","Lecturer","Married",56)
print(employee3.fullname, employee3.status, employee3.position, employee3.age)





