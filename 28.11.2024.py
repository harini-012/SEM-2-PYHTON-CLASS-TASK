#1
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

#2
class Inventory:
    def __init__(self,prodID,prodName,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID:", self.prodID)
        print("Product Name:", self.prodName)
        print("Prodyct Count", self.prodCount)
s=Show("E24AI012","Printer",100)
s.display()



#3
class Inventory:
    def __init__(self,prodID,prodName,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
class Show(Inventory):
    def display(self):
        print("Product ID:", self.prodID)
        print("Product Name:", self.prodName)
        print("Prodyct Count", self.prodCount)
s=Show("E24AI012","Printer",100)
s.display()
