class BankAccount:
    def __init__(self_kdm, balance):
        self_kdm.__balance_kdm = balance

    def deposit(self_kdm, amount):
        self_kdm.__balance_kdm += amount

    def withdraw(self_kdm, amount):
        if amount <= self_kdm.__balance_kdm:
            self_kdm.__balance_kdm -= amount
        else:
            print("Insufficient funds")

    def get_balance(self_kdm):
        return self_kdm.__balance_kdm

account = BankAccount(5000)
account.deposit(1000)
account.withdraw(2000)
print("Balance:", account.get_balance())

# Montes, Karen



