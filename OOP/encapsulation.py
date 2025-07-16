class Bankaccount:
    def __init__(self,name,balance):
        self.name=name  #public
        self.__balance=balance #private

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited amount : {amount}'\t'New balance : {self.__balance}")

    def withdraw(self,amount):
        self.__balance -= amount
        print(f"Withdrew amount : {amount}'\t'New balance : {self.__balance}")

bankacc = Bankaccount("Sneha",1000)
print('Acc holder : ',bankacc.name)
print('Balance : ',bankacc.get_balance())
bankacc.deposit(100)
bankacc.withdraw(600)
