import sys

class Bank:
    bankname = "A P Bank"
    branch = "Sector 18 Noida"

    def __init__(self, username, pan, address, pin, biometric_enabled=False):
        self.__username = username
        self.__pan = pan
        self.__address = address
        self.__balance = 0.0
        self.__transactionhistory = []
        self.__biometric_enabled = biometric_enabled
        self.__pin = pin
        self.__authenticated = False
        print(f"Congratulations, {self.__username}! Your account is created successfully")
        print(f"Name: {self.__username}")
        print(f"PAN: {self.__pan}")
        print(f"Address: {self.__address}")
        print(f"Balance: {self.__balance}\n")

    def authenticate_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.__pin:
            print("PIN authentication successful!")
            self.__authenticated = True
        else:
            print("PIN authentication failed. Access denied.")

    def authenticate_biometric(self):
        if self.__biometric_enabled:
            # Simulating biometric authentication
            biometric_input = input("Scan your fingerprint or enter biometric data: ")
            # Add your biometric authentication logic here
            if biometric_input == "valid_biometric_data":
                print("Biometric authentication successful!")
                self.__authenticated = True
            else:
                print("Biometric authentication failed. Access denied.")
        else:
            self.__authenticated = True

    def authenticate(self):
        self.authenticate_pin()
        if not self.__authenticated:
            return
        self.authenticate_biometric()

    def deposit(self, amount):
        self.authenticate()
        if self.__authenticated:
            self.__balance += amount
            self.__transactionhistory.append(('Deposit:', amount, 'Current balance:', self.__balance))
            print(f"{amount} deposited successfully\n")
        else:
            print("Authentication failed. Deposit not allowed.\n")

    def withdraw(self, amount):
        self.authenticate()
        if self.__authenticated:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__transactionhistory.append(("Withdraw:", amount, "Current balance:", self.__balance))
                print(f"{amount} withdrawn successfully\n")
            else:
                print(f"Insufficient balance! You have {self.__balance} in your account but you want to withdraw {amount}\n")
        else:
            print("Authentication failed. Withdrawal not allowed.\n")

    def ministate(self):
        print(f"Current balance: {self.__balance}")
        for transaction in self.__transactionhistory:
            print(transaction)
        print("\n")

class BankManager:
    def __init__(self):
        self.accounts = []

    def create_account(self, username, pan, address, pin, biometric_enabled=False):
        account = Bank(username, pan, address, pin, biometric_enabled)
        self.accounts.append(account)
        return account

    def access_account(self, account):
        account.authenticate_pin()
        if account._Bank__authenticated:
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
                    print("Thank you for using our services....Have a great day!")
                    sys.exit()
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Wrong PIN ")

manager = BankManager()

while True:
    print("1. Create Account\n2. Access Account\n3. Stop")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = input("Enter the username: ")
        pan = input("Enter the PAN: ")
        address = input("Enter the address: ")
        pin = input("Set your PIN: ")
        biometric_enabled = input("Enable biometric authentication? (yes/no): ").lower() == "yes"
        account = manager.create_account(username, pan, address, pin, biometric_enabled)
        print("Account created successfully!\n")
    elif choice == 2:
        if not manager.accounts:
            print("No accounts available. Please create an account first.")
        else:
            for i, acc in enumerate(manager.accounts, start=1):
                print(f"{i}. {acc._Bank__username}")
            acc_index = int(input("Enter the account number to access: "))
            if 0 <= acc_index < len(manager.accounts):
                manager.access_account(manager.accounts[acc_index])
            else:
                print("Invalid account number.\n")
    elif choice == 3:
        print("Thank you for using our services....Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
