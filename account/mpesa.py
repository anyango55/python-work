class account:
	def_init_(self,first_name,last_name,balance):
			self.first_name = first_name
			self.last_name = last_name
			self.balance = balance
	def welcome(self):
			return "dear, {} {} your count balace is{}".format(self.first_name,self.last_name,self.balance)
	def deposite(self,current_balance):
		deposite = current_balance
		self.balance = self.balance+current_balance
			return "dear, {} {} your count balace is{}".format(self.first_name,self.last_name,self.balance)
	def withdraw(self,y):
		withdraw=y
		if y > self.balance:
			return "not successsful"
		else:
			self.balance = self.balance-y
			return "dear,{} {} your account balance is{}".format(self.first_name,self.last_name,y)
	def showbalance(self):
		showbalance = self.balance
		return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)
