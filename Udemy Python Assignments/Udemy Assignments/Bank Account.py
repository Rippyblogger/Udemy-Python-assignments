class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_input(cls):
        return cls(
            input("owner: "),
            float(input('amount:')),
        )

    def __str__(self):
        return f"Owner is {self.owner}\nBalance is {self.balance}"
    def deposit(self, dep_amount):
        dep_amount = float(input("Enter intended amount for deposit:  "))
        if dep_amount < 0:
            return "Please input the deposit amount"
        else:
            self.balance += dep_amount
            print("New balance is: " + str(self.balance))

    def withdraw(self, withdraw_amount):
        withdraw_amount = float(input("Enter intended amount for withdrawal"))
        if withdraw_amount > self.balance:
            print("Intended withdrawal exceeds current account balance")
        else:
            self.balance -= withdraw_amount
            print("Your new account balance is: " + str(self.balance))






Funke = Account.from_input()
print(Funke)
Funke.deposit(2000)
Funke.withdraw(150000)