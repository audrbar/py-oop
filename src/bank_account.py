class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    def display_balance(self):
        print(f'Your balance: {self.balance}')


account = BankAccount('audrius', 500)
print(f'{account.owner} account balance {account.balance}')
account.deposit(5)
account.display_balance()
account.withdraw(10)
account.display_balance()
