from datetime import datetime

class account():
    def __init__(self, name, address, indeposit):
        self.name = name
        self.address = address
        self.balance = indeposit
    
    def checkbalance(self):
        print(f"{self.name}'s balance is £{self.balance}")
    
    def changename(self, new_name):
        print(f"Name changed from {self.name} to {new_name}")
        self.name = new_name
    

class gold_account(account):
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn £{amount}")
    
    def addinterest(self):
        interest = 1.01
        self.balance *= interest
        print(f"Interest added: {datetime.now()}")
    





account1 = account("James", "3, Oxford road", 10)
account2 = gold_account("Kevin", "6, Oxford road", 750)

account1.checkbalance()
account2.addinterest()

account1.changename("Bob")
account2.checkbalance()

account2.withdraw(100)

account1.checkbalance()
account2.checkbalance()

