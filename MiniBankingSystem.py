from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount} (Savings)")

class CryptoAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} added {amount} (Crypto)")

def add_money(account, amount):
    account.deposit(amount)

s1 = SavingsAccount("Awais", 500)
c1 = CryptoAccount("Ali", 100)

add_money(s1, 200)
add_money(c1, 50)   

print(f"{s1.name} Balance: {s1.balance}")
print(f"{c1.name} Balance: {c1.balance}")