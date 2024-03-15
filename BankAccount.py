class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Example usage:
account1 = BankAccount("123456", 1000)
account1.deposit(500)
account1.withdraw(200)
print("Balance:", account1.balance)
