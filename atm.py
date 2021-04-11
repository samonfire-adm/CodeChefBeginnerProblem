print("Enter The Value to be Withdrawl in $")
userInput = float(input())
userInput = round(userInput,2)
print("Enter The Amount You Have")
balance = float(input())
balance=round(balance,2)
bankCharge = 0.50
if (userInput%5 ==0) and (userInput>balance):    
    updatedbalance = balance
    print(f"Entered value Exceded The Remaining value is {updatedbalance} ")
elif userInput % 5 ==0:
	updatedbalance = balance - (userInput+bankCharge)
	print(f"The Remaining Balance is {updatedbalance}")
else:
    print("The amount entered for withdrawl is Not a multiple of 5")
    updatedbalance = balance
    print(f"The Remaining balance is {updatedbalance}")
