
#hybrid inheritance
class Employee:
    def __init__(self,emp_id):
        self.emp_id=emp_id
    def display_emp(self):
        print("EMPLOYEE ID",self.emp_id)
class Manager(Employee):
    def __init__(self,m_id):
        self.m_id=m_id
    def display_man(self):
        print("Manger id:",self.m_id)
class Owner(Employee):
    def __init__(self,own_id):
        self.own_id=own_id
    def display_own(self):
        print("Owner ID",self.own_id)
class Company(Employee,Manager,Owner):
    def __init__(self,emp_id,m_id,own_id):
        Employee.__init__(self,emp_id)
        Manager.__init__(self,m_id)
        Owner.__init__(self,own_id)
    def display_com(self):
        self.display_emp()
        self.display_man()
        self.display_own()
        
s=Company("e24ai012","m24ai012","o24ai012")
s.display_com()
