###   $$$$$$\ $$$$$$$$\ $$\      $$\        $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$\ $$$$$$$\ $$$$$$$$\ 
###  $$  __$$\\__$$  __|$$$\    $$$ |      $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$  __$$\\__$$  __|
###  $$ /  $$ |  $$ |   $$$$\  $$$$ |      $$ /  \__|$$ /  \__|$$ |  $$ |  $$ |  $$ |  $$ |  $$ |   
###  $$$$$$$$ |  $$ |   $$\$$\$$ $$ |      \$$$$$$\  $$ |      $$$$$$$  |  $$ |  $$$$$$$  |  $$ |   
###  $$  __$$ |  $$ |   $$ \$$$  $$ |       \____$$\ $$ |      $$  __$$<   $$ |  $$  ____/   $$ |   
###  $$ |  $$ |  $$ |   $$ |\$  /$$ |      $$\   $$ |$$ |  $$\ $$ |  $$ |  $$ |  $$ |        $$ |   
###  $$ |  $$ |  $$ |   $$ | \_/ $$ |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$$$$$\ $$ |        $$ |   
###  \__|  \__|  \__|   \__|     \__|$$$$$$\\______/  \______/ \__|  \__|\______|\__|        \__|   
###                                  \______|                                                       
'''START OF SCRIPT'''
import sys

###Account variable already provided in script:
account_balance = float(500.25)

### Withdraw amount variable created as place-holder for the while loop lower in the script:
withdraw_amount = float(0.0)

### Print balance Function created to output account balance:
def printbalance(acct_balance):
  return print("Your current balance:\n%.2f" % account_balance)

### Deposit Function created to calculate new account balance with deposit amount:
def deposit(acct_balance):
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  if deposit_amount <= 0.0:
    print("Invalid amount")
  else:
    new_account_balance = account_balance + deposit_amount
    return print("Deposit was $%.2f, current balance is $%.2f" % (deposit_amount, new_account_balance))
  
### Withdrawal Function created to calculate new account balance:
def withdraw(account_balance, withdraw_amount):
  withdraw_amount = float(input("How much would you like to withdraw today?\n"))
  
  ### Conditional statement if withdrawal amount exceeds account balance:
  if withdraw_amount > account_balance:
    print("$%.2f is greater than your account balance of $%.2f" % (withdraw_amount, account_balance))
    
  ### Conditional elif statement if withdrawal amount is less than or equal to new account balance:
  elif withdraw_amount <= account_balance:
    new_account_balance = account_balance - withdraw_amount
    return print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, new_account_balance))

### Created a userchoice variable with an empty string type for the while loop:
userchoice = ''

### Created while loop to continue transactions until 'Q' is selected:
while userchoice != 'Q':
  
  ### Createn userchoice variable to accept user input of 'D', 'W', 'B' or 'Q':
  ### Also note that user input will be formatted to accept lower-case letters with the .upper() method:
  userchoice = input("What would you like to do?\n").upper()

  ### Conditional statement if user selects 'D' execute deposit function:
  if (userchoice == 'D'):
    deposit(account_balance)
  
  ### Conditional statement if user selects 'W' execute withdrawal function:
  elif (userchoice == 'W'):
    withdraw(account_balance, withdraw_amount)
  
  ### Conditional statement if user selects 'B' execute printbalance function:
  elif (userchoice == 'B'):
    printbalance(account_balance)
  
  ### Conditional statement if user selects 'Q' execute print statement:
  elif (userchoice == 'Q'):
    print("Thank you for banking with us.")
'''END OF SCRIPT'''
