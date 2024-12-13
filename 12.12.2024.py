'''import random
class Customer:
    def __init__(self,cust_id,name,phoneno):
        self.cust_id=cust_id
        self.name=name
        self.phoneno=phoneno
    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"'''
def verify_customer_id():
        cust_id=input()
        cus_len=len(cust_id)
        if cus_len==8:
            if cust_id[0]=="T" and cust_id[1]=="I" and cust_id[2]=="C" and cust_id[3]=="K":
                if cust_id[4] and cust_id[5] and cust_id[6] and cust_id[7].isdigit()  ==True:
                    print("Valid")
                else:
                    print("last 4 cases not valid")
            else:
                print("first 4 cases not valid")
        else:
            print("length not valid")
verify_customer_id()
        
        
        

















print("*********************Welcome to TICKET booking application***************")
cust_id=input("Enter the customer id:")

