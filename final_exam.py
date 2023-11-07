class Bank:
    
    def __init__(self,name):
        self.name=name
        self.totalBalance=0
        self.totalLoan=0
        self.loanfacility=True
        self.accounts=[]
    
    def createAccount(self,name,email,type):
        account=Account(name,email,type)
        self.accounts.append(account)
        return account
    
    def deleteAccount(self,accountNo):
        for account in self.accounts:
            if account.accountNo==accountNo:
                self.accounts.remove(account)
                del account
                return
        print("No Account Found to delete !")
        
    def showUsers(self):
        for account in self.accounts:
            print(f"Account Number: {account.accountNo} of {account.name}")
    
    def showTotalBalance(self):
        print(f"Tolal Available Balance: {self.totalBalance}")
    
    def showTotalLoan(self):
        print(f"Current Tolal Loan: {self.totalLoan}")
    
    def offLoan(self):
        self.loanfacility=False
    
    def onLoan(self):
        self.loanfacility=True
    
    
        
class Account:
    
    generateAccountNumber=0
    
    def __init__(self,name,email,type):
        self.name=name
        self.email=email
        Account.generateAccountNumber+=1
        self.accountNo=Account.generateAccountNumber
        self.type=type
        self.transactions=[]
        self.balance=0
        self.loanCount=0
        self.loanAmount=0
        self.transactionId=self.accountNo*1000
        
        
    def checkBalance(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.accountNo}")
        print(f"Balance: {self.balance}")
    
    def transfer(self,bank,accNo,amount):
        for account in bank.accounts:
            if accNo==account.accountNo:
                other=account
                if self.balance>=amount:
                    self.balance-=amount
                    other.balance+=amount
                    print(f"Transferred {amount} from {self.name} to {other.name}")
        
                    transaction={}
                    self.transactionId+=1
                    transaction['id']=self.transactionId
                    transaction['type']="transfer"
                    transaction['from']=self.name
                    transaction['to']=other.name
                    transaction['amount']=amount
            
                    self.transactions.append(transaction)

                else:
                    print(f"Insufficient Amount !")
                
                return
        
        print("Inavalid Account to Transfer !")
                
        
        
    
    def deposit(self,bank,amount):
        if amount>0:
            bank.totalBalance+=amount
            self.balance+=amount
            
            transaction={}
            self.transactionId+=1
            transaction['id']=self.transactionId
            transaction['type']="deposit"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
            
        else:
            print(f"Invalid amount !")
        
    
    def withdraw(self,bank,amount):
        if amount>0 and bank.totalBalance>=amount and self.balance>=amount:
            bank.totalBalance-=amount
            self.balance-=amount
            
            transaction={}
            transaction['id']=self.transactionId+1
            transaction['type']="withdraw"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
            
        else:
            print(f"Invalid amount !")
    
    
    def takeLoan(self,bank,amount):
        if bank.loanfacility==True and amount>0 and bank.totalBalance>=amount and self.loanCount<2:
            self.loanAmount+=amount
            self.loanCount+=1
            bank.totalLoan+=amount
            
            transaction={}
            self.transactionId+=1
            transaction['id']=self.transactionId
            transaction['type']="loan"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
        
        else:
            print(f'Invalid Loan Request !')
    
    def showTransactions(self):
        print(f"Transaction History of {self.name}:")
        
        for transaction in self.transactions:
            if 'to' in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']} to {transaction['to']}")
            
            elif 'id' in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']}")




bank=Bank("Madhumoti Bank Ltd.")
admin=bank.createAccount("admin","admin#gmail.com","admin")


currentUser=admin
changeOfUser=True

while True:
    
    if currentUser==None:
        print("\n\t--->!!! No logged in user\n")
        
        option=input("Login or Register (L/R) :")
        
        if option =="L":
            id=int(input("\tEnter Account Number:"))
            
            
            match=False
            for user in bank.accounts:
                if user.accountNo==id:
                    currentUser=user
                    changeOfUser=True
                    match=True
                    break
            if match==False:
                print("\n\t---> No user Found !\n")
                
        elif option == "R":
            name=input("\tEnter Name:")
            email=input("\tEnter E-mail:")
            type=input("\tAccount Type (Savings/Current):")
            
            user=bank.createAccount(name,email,type)
            
            currentUser=user
            changeOfUser=True
    
    else:
        if changeOfUser:
            print("\n------------------------------------")
            print(f"\tWelcome Back {currentUser.name} !")
            print("------------------------------------")
            changeOfUser=False
        else:
            print("\n\t<---------------------------->")
        
        if currentUser.name=="admin":
                        
            print("Options:\n")
            print("1: Create Account")
            print("2: Delete Account")
            print("3: Show Users")
            print("4: Check Total Balance")
            print("5: Check Total Loan")
            print("6: On Loan facility")
            print("7: Off Loan facility")
            print("8: Log Out")
             
             
            ch=int(input("\nEnter Option:"))
             
            if ch==1:
                name=input("\tEnter Name:")
                email=input("\tEnter E-mail:")
                type=input("\tAccount Type (Savings/Current):")
                 
                bank.createAccount(name,email,type)
                 
            elif ch==2:
                accNo=int(input("\tEnter Account Number:"))
                bank.deleteAccount(accNo)
                  
            
            elif ch==3:
                bank.showUsers()
            
            elif ch==4:
                bank.showTotalBalance()
            
            elif ch==5:
                bank.showTotalLoan()
            
            elif ch==6:
                bank.onLoan()
            
            elif ch==7:
                bank.offLoan()
             
            elif ch==8:
                currentUser=None
             
            else:
                print("\n\t---> !!! Choose Valid Option\n")
                  
        
        else:
            print("Options:\n")
            print("1: Deposit")
            print("2: Withdraw")
            print("3: Check Balance")
            print("4: Check Transactions History")
            print("5: Take Loan")
            print("6: Tarnsfer")
            print("7: Logout")
            
            ch=int(input("\nEnter Option:"))
            
            if ch==1:
                amount=int(input("\tEnter Amount:"))
                currentUser.deposit(bank,amount)
            
            elif ch==2:
                amount=int(input("\tEnter Amount:"))
                currentUser.withdraw(bank,amount)
                
            elif ch==3:
                currentUser.checkBalance()
                
            elif ch==4:
                currentUser.showTransactions()
            
                
            elif ch==5:
                amount=int(input("\tEnter Amount:"))
                currentUser.takeLoan(bank,amount)
            
            elif ch==6:
                accNo=int(input("\tEnter Account to Transfer:"))
                amount=int(input("\tEnter Amount:"))
                
                currentUser.transfer(bank,accNo,amount)
                
            elif ch==7:
                currentUser=None
                
            else:
                print("\n\t---> !!! Choose Valid Option\n")
                    
