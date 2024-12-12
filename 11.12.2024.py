#ENCAPSULATION
class Student:
    id=123 #class variable
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name:",self.__name)
s=Student("Ria")
s.display()
#print(s.__name)#it will show the error because it is private
print(s.id)# it is class variable and public so the print statement will be excecuted


#USER INPUT
class Student:
    id=int(input("Enter the id of the student"))
    def __init__(self):
        self.__name=input("Enter the name of the student")
        self.__age=int(input("Enter the age of the student"))
    def display(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
s=Student()
s.display()
print(s.id)


# NAME MANGLING(obj._Classname__variable in private)
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
emp=Employee('Jessa',10000)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)# to view the particular information which is prive without using the display method 



# USER INPUT
class Teacher:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
name=input("Enter the teacher name")
salary=int(input("Enter the teacher salary"))
t=Teacher(name,salary)
print("Name of the teacher is",t.name)
print("Salary of the teacher is",t._Teacher__salary)


#INHERITANCE WITH NAME MANGLING 
class Teacher:
    def __init__(self):
        self.name="Harini"
        self.__salary=10000
    
class Student(Teacher):
    def __init__(self):
        Teacher.__init__(self)
        self.stu_id="E24AI012"
    def displayStudent(self):
        print("Name:",self.name)
        print("Student id:",self.stu_id)
        

s=Student()
s.displayStudent()
print(s._Teacher__salary)
