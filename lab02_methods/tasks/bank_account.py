class BankAccount:
    """Задача: bank_account"""
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance = self.balance + amount

    def withdraw(self, amount: int):
        """Снимает только если достаточно средств"""
        if self.balance>=amount:
            self.balance = self.balance - amount
            return True
        else:
            return False
