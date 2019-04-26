class MpesaAccount:
    def __init__(self,name,phone_number,balance):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.deposits= []
        self.withdrawals = [] 
        self.loan = 0
        self.cash = []
    def withdrawal_amount(self,m):
        withdrawal_amount = m
        if m>self.balance:
            print("balance insufficent")
        else:
            self.balance = self.balance - m

            self.withdrawals.append(m)
            return "hello {} withdwawal of amount{}successful".format(self.name,m,self.balance)
            print(name)
    def deposit(self,n):
        deposit = n
        self.balance = self.balance + n
        self.deposits.append(n)
        desit = "Hello {} deposit of cash {} was successful balance is {}".format(self.name,n,self.balance)
        print(desit)
    def check_balance(self):
        check_balance = self.balance
        bal = "Hello {} balance is {}".format(self.name,self.balance)
        print(bal)
    def my_deposits(self):
        for n in self.deposits:
            print(n)
            
    def my_withdrawals(self):
        for m in self.withdrawals:
            print(m)
    def give_loan(self,amount):
        loan = amount
        if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
            self.loan = self.loan + amount
            print("Great,your loan of {} has been approved".format(amount))
        else:
            print("we are sorry, your loan of  {} has not been approved ".format(amount))
    def repayment(self,cash):
        if cash<self.loan:
            self.loan = self.loan-cash
            print("Hello you can repay your loan multiple times".format(self.loan))
        elif cash>self.loan:
            self.loan = self.loan - cash
            print("Hello  your cash deposit is {} thus your standing loan balance is {}".format(self.deposits,self.loan))
        elif excesscash > self.loan:
             check_balance = excesscash + balance
             print("Hello you overpayed {} hence your current balance is {}".format(self.cash,self.balance))
    
    

    



    

        
