class Atm:
    def __init__(self, name, cardNumber, pin, wallet, balance):
        self.name = name
        self.cardNumber = cardNumber
        self.pin = pin
        self.wallet = int(wallet)
        self.balance = int(balance)

    def check_balance(self):
        print("You have " + str(self.balance) + " dollars in your bank account!")

    def withdraw_money(self):
        howMuch = int(input("How much would you like to withdraw from your bank account? "))

        if howMuch > self.balance:
            print("You do not have that much money in your bank account!")
        else:
            self.balance -= howMuch
            self.wallet += howMuch
            print("You have " + str(self.balance) + " dollars in your bank account and " + str(self.wallet) + " in your wallet.")

userName = input("What is your name? ")

userCardNum = input("What is your card number? ")

userPin = input("What is your pin? ")

userWalletAmount = input("How much do you have in your wallet? ")

userBalance = input("How much do you have in your bank account? ")

personNew = Atm(userName, userCardNum, userPin, userWalletAmount, userBalance)

personNew.check_balance()
personNew.withdraw_money()
