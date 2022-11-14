class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname," Your Account ",self.acno," Is Opened With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry You Need Another ",self.needs," Rs.")
    def checkBalance(self):
        print("Curret Balance : ",self.balance)

b1=Bank()
acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance : "))

b1.openAccount(acno,cname,balance)

while True:

    print("*"*40)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*40)

    choice=int(input("Enter Your Choice : "))
    print("*"*40)
    
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*40)

    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*40)

    elif choice==3:
        b1.checkBalance()
        print("*"*40)

    else:
        print("Good By")
        break
