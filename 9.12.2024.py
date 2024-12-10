
#HYBRID INHERITANCE
class Employee:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print("Name of the employee:",self.name)
        print("Age of the employee:",self.age)
class Manager(Employee):
    def _init_(self,name,age,eid):
        Employee._init_(self,name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("ID:",self.eid)
class Developer(Employee):
    def _init_(Self,name,age,dept):
        Employee._init_(self,name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department:",self.dept)
class TeamLeader(Manager,Developer):
    def _init_(self,name,age,eid,dept,teamsize):
         Employee._init_(self,name,age)
         self.eid=eid
         self.dept=dept
         self.teamsize=teamsize
    def displayTeamInfo(self):
        print("Team size={self.Teamsize}")
Name=input()#we can use different cases here
Age=int(input())
Eid=input()
Dept=input()
ts=input()
tl=TeamLeader(Name,Age,Eid,Dept,ts)
tl.displayEmployeeInfo()
