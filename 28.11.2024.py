 class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the id:")
        self.name=input("enter the name")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary=",self.sal)


p=Perks()
p.getDetails()
p.displayInfo()




class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter id")
        self.name=input('Enter the name')
        self.salary=int(input('Enter the salary'))
    def displayEmployeeInf(self):
        print(f"ID={self.id}\n Name={self.name} \nSalary={self.salary}")
    def getSalary(self):
        return self.salary
class Perks(Employee):
    def calculatesalary(Self):
        self.getEmployeeInfo()
        sal=self.getSalry()
        self.hra=sal*/
        self.total=self.hra+self.da
    def displayPerks(self):
        self.displayEmpl
        
