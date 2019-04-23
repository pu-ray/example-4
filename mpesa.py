class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance
	def withdrawal_amount(self,m):
		withdrawal_amount=m
		self.balance = self.balance-m
		amant =" Hello {} withdrawal of cash {} was successful balance is {}".format(self.name,m,self.balance)
		print(amant)
	def deposit(self,n):
		deposit = n
		self.balance = self.balance + n
		desit = "Hello {} deposit of cash {} was successful balance is {}".format(self.name,n,self.balance)
		print(desit)
	def check_balance(self):
		check_balance = self.balance
		bal = "Hello {} balance is {}".format(self.name,self.balance)
		print(bal)
	

		
