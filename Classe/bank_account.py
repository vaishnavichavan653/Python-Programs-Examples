class BankAccount:
    count = 1000

    def __init__(self, name):
        self.name = name
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money.")

    def display_balance(self):
        print(self.name, "has", self.balance)

    def transfer(self, amount, other):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Not enough money to transfer.")


account1 = BankAccount("Asha")
account2 = BankAccount("Ravi")

account1.deposit(500)
account1.withdraw(50)
account1.transfer(100, account2)
account1.display_balance()
account2.display_balance()
