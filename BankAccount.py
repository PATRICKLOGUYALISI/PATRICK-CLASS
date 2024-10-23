class BankAccount:
    interest_rate = 0.05

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance is {self.balance}.")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


account1 = BankAccount("Ade Amos")
account2 = BankAccount("Muloki Joseph")
account3 = BankAccount("Patrick loguya")

account1.deposit(1000)
account1.withdraw(200)
account1.apply_interest()
account1.display_account_info()

account2.deposit(1500)
account2.withdraw(500)
account2.apply_interest()
account2.display_account_info()

account3.deposit(600000)
account3.withdraw(250000)
account3.apply_interest()
account3.display_account_info()
