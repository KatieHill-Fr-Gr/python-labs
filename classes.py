
import random

# * Superclass

class BankAccount():
    def __init__(self, owner, balance, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount
        print(f'Your balance is now {self.balance}')
    
    def withdraw(self, amount):
        if (self.has_overdraft == False and self.balance < amount):
            print('Sorry, we were unable to process your request due to insufficient funds')
        elif (self.has_overdraft == True):
            self.balance -= amount
            print(f'Your balance is now {self.balance}')

myAccount = BankAccount('Katie', 4000, False)

print(myAccount)

myAccount.deposit(100) # Call the method on your object or "instance"
myAccount.withdraw(4500)
    

# * Subclass

class SavingsAccount(BankAccount):
    def withdraw(self):
        return "No withdrawals permitted"
    

saver = SavingsAccount("Katie", 100)
print(saver.withdraw())