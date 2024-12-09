class Student:
    def __init__(self):
        self.name=input()
        self.age=int(input())
class Mark(Student):
    def __init__(self):
        Student.__init__(self)
        self.mark1=int(input())
        self.mark2=int(input())
    def percentage(self):
            self.total=self.mark1+self.mark2
            self.per=(self.total/200)*100
    def display_details(self):
            print("Name:",self.name)
            print("Age:",self.age)
        
            print("Total:",self.total)
            print("Percentage:",self.per)
s=Mark()
s.percentage()
s.display_details()
