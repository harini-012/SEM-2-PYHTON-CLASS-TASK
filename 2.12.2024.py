#MULTILEVEL INHERITANCE

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name:",self.name,"\nId:",self.age)
class Employee(Person):
    def __init__(self,name,age,Id):
        Person.__init__(self,name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id:",self.Id)
class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        Employee.__init__(self,name,age,Id)
        self.salary=salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary:",self.salary)
m=Manager("Harini",18,"E24AI012",100000)
m.displayManager()



class Director:
    def __init__(self,Director_name,film_name):
        self.Director_name=Director_name
        self.film_name=film_name
    def displayDirector(self):
        print(f"Director Name:{self.Director_name},\nFilmName:{self.film_name}")
class Producer(Director):
    def __init__(self,Director_name,film_name,producer_name):
        Director.__init__(self,Director_name,film_name)
        self.producer_name=producer_name
    def displayProducer(self):
        self. displayDirector()
        print("Producer Name:",self.producer_name)
class Editor(Director):
    def __init__(self,Director_name,film_name,Editor_name):
        Director.__init__(self,Director_name,film_name)
        self.Editor_name=Editor_name
    def displayEditor(self):
        print("Editor Name:",self.Editor_name)
film=Editor("manirathnam","ponniyin selvan","Rickshitha")
film2=Producer("manirathnam","ponniyin selvan","sunpictures")
film.displayEditor()
film2.displayProducer()
