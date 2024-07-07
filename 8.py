#	Implement a Python class named BankAccount representing a bank account,
#   incorporating attributes such as accountNumber, name, and balance. Provide 
#   a complete code for the BankAccount class with various methods.

class BankAccount:
    def __init__(self,AccountNumber,name,Balance=0):
        self.AccountNumber=AccountNumber
        self.name=name
        self.Balance=Balance
    
    def Deposite(self,amount):
        self.Balance+=amount
        return self.Balance
    
    def Withdraw(self,amount):
        if amount>self.Balance:
            print("Insufficiant Balance")
            return
        self.Balance-=amount
        return self.Balance
    
    def display(self):
        print("Account Number:",self.AccountNumber)
        print("Name:",self.name)
        print("Balance:",self.Balance)

obj=BankAccount("1135010314305","kishu kumar",5000)
obj.Deposite(1000)
obj.Withdraw(5444)
obj.display()
