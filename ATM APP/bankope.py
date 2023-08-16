from bankerror import *
import random

accounts={}
balance={}
def generate_pin():
	return random.randint(1000, 9999)

def create_account():
	return random.randint(1000, 9999)

def balenq(account_number):
	if account_number in balance:
		print("available balance: ",balance[account_number])
	else:
		print("Invalid account number")
def deposit(account_number):
	amt=float(input("Enter Deposit Amount: "))
	if account_number in balance:
		if(amt<=0):
			raise DepositError
		else:
			balance[account_number]=balance[account_number]+amt
			print("Deposit Amount is: ",amt)
			print("Total Available Balnce: ",balance[account_number])
	else:
		print("Invalid account number")
def withdrawal(account_number):
	amt=float(input("Enter Withdwraw Amount: "))
	if account_number in balance:
		if(amt<=0):
			raise WithDrawalError
		elif(amt>balance[account_number]):
			raise InSufficientBalanceError
		else:
			balance[account_number]=balance[account_number]-amt
			print("Withdrawal Amount",amt)
			print("Available Balance",balance[account_number])

	else:
		print("Invalid account number")
