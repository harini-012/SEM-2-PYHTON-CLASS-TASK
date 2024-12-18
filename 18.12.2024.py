#Magic method add:
class Book:
    def __init__(self,pages):
        self.pages=pages
    #Overloading + operator with magic  method for object
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(300)
print("Total numebr of pages:",b1+b2)




#Method overloading using none
class Addition:
    def add(self,a,b,c=None):
        result=0
        if a!=None and b!=None and c==None:
            result=a+b
            return result
        elif a!=None and b!=None and c!=None:
            result=a+b+c
            return result
ad=Addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add(1,2,3)
print(ans1)
        


#Method overloading using zero
class Addition:
    def add(self,a,b,c=0):
        result=0
        result=a+b+c
        return result
ad=Addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add(1,2,3)
print(ans1)
        
