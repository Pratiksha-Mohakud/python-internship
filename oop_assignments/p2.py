# creating a class
class BankAccount():
    def __init__(bank,account_number,account_holder,balance): # initializing the attributes
        
        bank.acc_no=account_number
        bank.acc_holder=account_holder
        bank.balance=balance

# defining methods under class

    def deposit(bank,amount):
        bank.amount=amount
        bank.balance+=bank.amount
    def withdraw(bank,amount):
        if 0<amount<=bank.balance and bank.balance!=0:
            bank.amount=amount
            bank.balance-=bank.amount
        else: print("can't process payment")
    def get_balance(bank):
        return bank.balance
    
# taking inputs from the user
account_number=input("Enter your bank account number: ")
account_holder=input("Enter the name of account holder: ")
balance=int(input("Enter current balance: "))

obj=BankAccount(account_number,account_holder,balance)  # passing the inputs to class 
choice=int(input("1.Make a deposit\n2.Make a withdrawal\n3.Check balance\n"))

# asking choice of the user to use the class methods
match choice:
    case 1:
        amount=int(input("Enter amount to deposit: "))
        obj.deposit(amount)
        print(f"Deposited,current balance is {obj.balance}")
    case 2:
        amount=int(input("Enter amount to withdraw: "))
        obj.withdraw(amount)
        print(f"Withdrawal done,current balance is {obj.balance}")
    case 3: 
        print(obj.get_balance())



        