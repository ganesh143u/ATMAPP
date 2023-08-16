from ATMMenu import menu
from bankerror import *
from bankope import *
import sys
while(True):
	print()
	try:
		menu()
		n=int(input("\tEnter your choice (1/2/3/4/5): " ))
		if(n==1):
			account_number=len(accounts)+1
			pin=generate_pin()
			accounts[account_number]=pin
			balance[account_number]=500
			print(f"Account created successfully.\nAccount Number: {account_number}\nPIN: {pin}")
		
		elif(n==2):
			account_number=int(input("Enter your Account Number: "))
			balenq(account_number)
		elif(n==3):
			try:
				account_number = int(input("Enter your account number: "))
				deposit(account_number)
			except DepositError:
				print("Please Do Not Enter 0 or -ve amount")
			except ValueError:
				print("Enter Valid Amount")
		elif(n==4):
			try:
				account_number = int(input("Enter your account number: "))
				withdrawal(account_number)
			except WithDrawalError:
				print("Please Do Not Enter 0 or -ve amount")
			except InSufficientBalanceError:
				print("Sufficient Balance is not Available")
			except ValueError:
				print("Enter Valid Amount")
		elif(n==5):
			print("\tThank you for using our ATM")
			print("\t Visit Again")
			sys.exit()
		else:
			print("\tInvalid choice Please select a valid option")
	except ValueError:
		print("Invalid input. Please enter a valid number")
			
				
		