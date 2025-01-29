class Maggi_pack:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check_budget(self,budget):
        if not  isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget cannot be neagative")
        return True
    def calculate_balance(self,budget):
        return budget-self.price
    def suggest_packs(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print(f"You can buy {self.name} pack")
                print(f"Your remaining balance is {self.calculate_balance(budget)}")
            elif budget==self.price:
                print(f"You can buy {self.name}.No balance is remaining")
            else:
                print(f"You will not be able to afford it.")
        except ValueError as e:
            print(e)
    
small=Maggi_pack("small",20)
regular=Maggi_pack("regular",30)
big=Maggi_pack("big",50)
packets=[small,regular,big]
try:
    budget=float(input("Enter the budget"))
    for pack in packets:
        pack.suggest_packs(budget)
except ValueError:
    print("Enter the numerical value")
