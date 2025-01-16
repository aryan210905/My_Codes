# Bank account System

class Account:
    def __init__(self,name,bankBalance,accNo):
        self.name = name
        self.bankBalance = bankBalance
        self.accNo = accNo

    def debit(self):
        self.printBankBalance()
        self.debit = int(input("Enter amount to debit: "))
        self.bankBalance = self.bankBalance - self.debit
        print(f"Successfully debited the money.")
        self.printBankBalance()

    def credit(self):
        self.printBankBalance()
        self.credit = int(input("Enter amount to credit: "))
        self.bankBalance = self.bankBalance + self.credit
        print(f"Successfully credited the money")
        self.printBankBalance()

    def printBankBalance(self):
        print(f"Current bank balance: {self.bankBalance}")

acc1 = Account("Aryan",10000,10)
acc2 = Account("Krish",20000,11)
acc3 = Account("Jay",30000,12)
acc4 = Account("Meet",14000,13)
acc5 = Account("Kamal",40000,14)

print("\nMenu:")
print("1.Debit")
print("2.Credit")
print("3.PrintData")
print("4.Exit")
choice = int(input("\nEnter choice: "))
match choice:
    case 1:
        acc = int(input("Enter account number: "))
        match acc:
            case 10:
                acc1.debit()
            case 11:
                acc2.debit()
            case 12:
                acc3.debit()
            case 13:
                acc4.debit()
            case 14:
                acc5.debit()
            case _:
                print("Invalid account number")
    case 2:
        acc = int(input("Enter account number: "))
        match acc:
            case 10:
                acc1.credit()
            case 11:
                acc2.credit()
            case 12:
                acc3.credit()
            case 13:
                acc4.credit()
            case 14:
                acc5.credit()
            case _:
                print("Invalid account number")
    case 3:
        acc = int(input("Enter account number: "))
        match acc:
            case 10:
                acc1.printBankBalance()
            case 11:
                acc2.printBankBalance()
            case 12:
                acc3.printBankBalance()
            case 13:
                acc4.printBankBalance()
            case 14:
                acc5.printBankBalance()
            case _:
                print("Invalid account number")
    case 4:
        raise SystemExit
    case _:
        print("Invalid choice")