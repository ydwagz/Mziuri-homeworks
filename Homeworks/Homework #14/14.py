class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, balance):
        if balance <= 0:
            print("oe brat ra minusebs miwer giji xuarxar")
        elif balance > 2500:
            print("no no no 2500 or less")
        else:
            self.balance += balance

    def withdraw(self, tanxa):
        if tanxa > self.balance:
            print("bodiShi, idealuri samyaro araa. tavi vin ggonia???")
        else:
            self.balance -= tanxa


    def display_balance(self):
        print(self.balance)

user_input = int(input("შემოიტანე შენი ფულები: "))
account = BankAccount("dachi razmadze", 20)
account.deposit(user_input)
account.display_balance()
tanxa = int(input("ramdenis gamotana ginda: "))
account.withdraw(tanxa)
account.display_balance()



print(issubclass(Triangle, Polygon))