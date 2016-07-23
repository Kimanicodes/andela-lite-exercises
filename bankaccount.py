class BankAccount(object):
    def __init__(self, balance):
        self.balance = int(balance)

    def deposit(self, amt):
        self.balance = self.balance + amt
        return self.balance

    def withdraw(self, amt):
        if amt > self.balance:
            return 'Overdraft baba'
        else:
            self.balance = self.balance - amt
            return self.balance


myaccount = BankAccount(1000)
trans1 = myaccount.deposit(500)
trans2 = myaccount.withdraw(800)
print (trans1)
print (trans2)

