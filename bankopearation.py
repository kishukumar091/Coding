class Bank:
    bankname = "A P Bank"
    branch = "Sector 18 Noida"

    def __init__(self, username, pan, address):
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0
        self.transactionhistory = []
        print(f"Congratulations, {self.username}! Your account is created successfully")
        print(f"Name: {self.username}")
        print(f"PAN: {self.pan}")
        print(f"Address: {self.address}")
        print(f"Balance: {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        self.transactionhistory.append(("Deposit", amount, "Current balance", self.balance))
        print(f"{amount} deposited successfully\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactionhistory.append(("Withdraw", amount, "Current balance", self.balance))
            print(f"{amount} withdrawn successfully\n")
        else:
            print(f"Insufficient balance! You have {self.balance} in your account but you want to withdraw {amount}\n")

    def ministate(self):
        print(f"Current balance: {self.balance}")
        for transaction in self.transactionhistory:
            print(transaction)
        print("\n")


class BankManager:
    def __init__(self):
        self.accounts = []

    def create_account(self, username, pan, address):
        account = Bank(username, pan, address)
        self.accounts.append(account)
        return account

    def access_account(self, account):
        while True:
            print("1. Deposit\n2. Withdraw\n3. Mini statement\n4. Switch account\n5. Stop")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = float(input("Enter the amount to be deposited: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to be withdrawn: "))
                account.withdraw(amount)
            elif choice == 3:
                account.ministate()
            elif choice == 4:
                break
            elif choice == 5:
                print("Thank you for using our services. Have a great day!")
                exit()
            else:
                print("Invalid choice. Please enter a valid option.")


manager = BankManager()


while True:
    print("1. Create Account\n2. Access Account\n3. Stop")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = input("Enter the username: ")
        pan = input("Enter the PAN: ")
        address = input("Enter the address: ")
        account = manager.create_account(username, pan, address)
        print("Account created successfully!\n")
    elif choice == 2:
        if not manager.accounts:
            print("No accounts available. Please create an account first.")
        else:
            print("Available Accounts:")
            for i, acc in enumerate(manager.accounts, start=1):
                print(f"{i-1}. {acc.username}")
            acc_index = int(input("Enter the account number to access: "))
            if 0 <= acc_index < len(manager.accounts):
                manager.access_account(manager.accounts[acc_index])
            else:
                print("Invalid account number.\n")
    elif choice == 3:
        print("Thank you for using our services. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
