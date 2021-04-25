'''______                                     __    _      __ 
  / ____/________  ________  _______  __     / /   (_)____/ /_
 / / __/ ___/ __ \/ ___/ _ \/ ___/ / / /    / /   / / ___/ __/
/ /_/ / /  / /_/ / /__/  __/ /  / /_/ /    / /___/ (__  ) /_  
\____/_/   \____/\___/\___/_/   \__, /____/_____/_/____/\__/  
                               /____/_____/
'''
'''START OF SCRIPT'''
###Created empty grocery_item Dictionary and empty grocery_history List:
grocery_item = {}
grocery_history = []

###Variable to check if the while loop condition is met:
stop = 'notstop'

###While loop to cycle through and add User data to the Dictionary:
while stop != 'q':
  ###Item name variable created using User input:
  item_name = input("Item name:\n")
  ###Quantity variable created using User input:
  quantity = input("Quantity purchased:\n")
  ###Per item cost variable created using User input:
  cost = input("Price per item:\n")
  ###Update the grocery_item Dictionary with the User input:
  grocery_item['name'] = item_name
  grocery_item['number'] = int(quantity)
  grocery_item['price'] = float(cost)
  ###Added grocery_item Dictionary to the grocery_history List with .append():
  grocery_history.append(grocery_item.copy())
  ###Changing the stop variable to reflect User input of 'c' for continue or 'q' for quit:
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

###Created grand_total variable to hold the sum of all items:
grand_total = 0

###For loop created to iterathe through the grocery_history: 
for item in (grocery_history):
  ###Item total variable created, multiplying number of items by the price of that item:
  item_total = item['number'] * item['price']
  ###Created grand total variable and added item total to that variable:
  grand_total += item_total
  '''Output the item number in the format of a digit, item name as a string, item price as an 
  integer formated to 2 decimal points and the item total for all purchased items formated to
  2 decimal points'''
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  
  ###Created the item total variable and stored it to 0:
  item_total = 0

###Output the grand total:
print('Grand total: $%.2f' % grand_total)
'''END OF SCRIPT'''
