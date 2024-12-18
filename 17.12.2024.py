#POLYMORPHISM


class Teacher:
    def __init__(self,name,qualification):
        self.name=name
        self.qualification=qualification
    def show(self):
        print("Details:",self.name,self.qualification)
    def covered_portions(self):
        print("The covered portions is 10 lessons")
    def number_tests(self):
        print("The number of tests conducted in the classroom is 50")
class Headmistress(Teacher):
   
    def covered_portions(self):
        print("The headmistress covered portions is 10")
    def number_tests(self):
        print("The number of tests by headmistress is 5")
h=Headmistress("Bagavathy","PHD")
h.show()
h.covered_portions()
h.number_tests()
t=Teacher("Savithri","MSC")
t.show()
t.covered_portions()
t.number_tests()



class Library:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is :{book_name} by {user}"
class DigitalLibrary:
    def issue_book(Self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is:{book_name} by {user}"
lib=Library()
dig=DigitalLibrary()
book=input()
username=input()
print(lib.issue_book(book,username))
print(lib.returned_book(book,username))
print(dig.issue_book(book,username))
print(dig.returned_book(book,username))





        
        
