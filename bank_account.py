class BankAccount:
    def __init__(self_kdm, account_name, balance):
        self_kdm.account_name_kdm = account_name
        self_kdm.balance_kdm = balance

    def deposit(self_kdm, amount):
        self_kdm.balance_kdm += amount
        print("Deposit successful")

    def withdraw(self_kdm, amount):
        if amount <= self_kdm.balance_kdm:
            self_kdm.balance_kdm -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self_kdm):
        print("Balance:", self_kdm.balance_kdm)

account = BankAccount("Ren", 50000)
account.deposit(5000)
account.withdraw(4000)
account.display_balance()

# Montes, Karen