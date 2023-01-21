class Account():
    def __init__(self,account_no):
        self.account_no= account_no
        self.balance= 0.0
    def display(self):
        self.account_no= str(self.account_no)
        self.nr= ""
        for x in range(len(self.account_no)):
            if x==2 or x==6 or x==10 or x==14 or x==18 or x==22:
                self.nr+=" "
            self.nr+=self.account_no[x]
        self.balance= round(self.balance,2)
        print(f"Bank account No: {self.nr}\nAccount balance: {self.balance}PLN")
    def deposit(self,amount):
        self.balance=float(self.balance)
        self.balance+=amount
    def withdraw(self,amount):
        self.balance=float(self.balance)
        if amount>self.balance:
            print("Insufficient funds on the account.")
        else: self.balance-=amount
