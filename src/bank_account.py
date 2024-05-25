class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance
        print(f"Success. {self.owner} account was created. Account balance: {self.balance}$.")

    def deposit(self, addition: int):
        self.balance += addition
        print(f"Success: {addition}$ was deposited. Current balance is: {self.balance}$.")

    def withdraw(self, subtraction: int):
        if subtraction > self.balance:
            print(f"Lack of resources. Balance is: {self.balance}$.")
        else:
            self.balance -= subtraction
            print(f"Success: {subtraction}$ was withdrawn. Current balance is: {self.balance}$.")

    def display_balance(self):
        print(f'{self.owner}, your balance is: {self.balance}')


account = BankAccount('audrius', 500)
account.deposit(50)
account.withdraw(60)
account.display_balance()
