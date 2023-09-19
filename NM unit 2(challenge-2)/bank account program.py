class Account:
    def __init__(self):
        self.balance=0
        print("hello!! welcome to your Account")
        print("your account holder name:XXXXX")
    def deposit(self):
            amount=int(input("enter amount to be deposited:"))
            self.balance+=amount
            print(" your new balance=%d"%self.balance)
    def withdraw(self):
        amount=int(input("enter an amount to be withdrawn:"))
        if (amount>self.balance):
            print(" insufficient balance")
        else:
            self.balance-=amount
            print("your remaining balance=%d" %self.balance)
    def enquiry(self):
         print("your balance =%d"%self.balance)
Account=Account()
Account.deposit()
Account.withdraw()
Account.enquiry()
            
