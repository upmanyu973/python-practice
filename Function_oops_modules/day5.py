# # OOP part 1: classes, __init__, instance vs class attributes, methods

# Exercise: Write a class BankAccount with a class attribute bank_name = "First Python Bank",
#  and an __init__ that takes owner and balance (default balance=0 if not given) and stores them as instance attributes. 
# Add a method deposit(self, amount) that adds amount to self.balance. 
# Create two accounts, deposit into one of them, and print both accounts' owner, balance,
#  and bank_name to confirm the class attribute is shared while balance/owner are independent.


class BankAccount:
    bank_name = "First Python Bank"

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount

a1 = BankAccount("Rishabh",10000)
a2 = BankAccount("Aarti", 30000)

a1.deposit(5000)

print(a1.owner, a1.balance, a1.bank_name)
print(a2.owner, a2.balance, a2.bank_name)
