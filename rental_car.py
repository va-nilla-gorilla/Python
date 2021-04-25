#################################################################
##       #       ##               ###     #######################
##       #       ##      #####     ##     #######################
##       #       ##      #####     ##     ######
##       #       ##               ###     ######
##       #       ##             #####     ##########
##       #       ##      ##      ####     ##########
##               ##      ##       ###     ######
##               ##      ###       ##     ######      ###
###             ###      ####       #     ######     #####
################################################      ###
'''START OF SCRIPT'''
import sys

# Rental Code Variable:
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()

# Number of Days/Weeks Rented According to rentalCode and rentalPeriod Input:
if rentalCode == "B" or rentalCode == "D":
    rentalPeriod = int(input("Number of Days Rented:\n"))
if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n"))

# Rental Car Pricing Based on rentalCode Variables:
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

# Odometer Start, Odometer End and totalMiles Driven Variables:
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = int(odoEnd) - int(odoStart)

# Mileage Calculations Based on rentalCode, rentalPeriod and extraMiles:
if rentalCode == "B":
    mileCharge = int(totalMiles) * 0.25

if rentalCode == "D":
    averageDayMiles = int(totalMiles) / int(rentalPeriod)
    if averageDayMiles <= 100:
        mileCharge = 0.00
    elif averageDayMiles > 100:
        extraMiles = averageDayMiles - 100
        mileCharge = extraMiles * 0.25
if rentalCode == "W":
    averageWeekMiles = int(totalMiles) / int(rentalPeriod)
    if averageWeekMiles <= 900:
        mileCharge = 0.00
    elif averageWeekMiles > 900:
        mileCharge = 100.00 * int(rentalPeriod)
        
# Base Charge Calculations for each rentalCode and rentalPeriod:
if rentalCode == "B":
    baseCharge = int(rentalPeriod) * float(budgetCharge)
elif rentalCode == "D":
    baseCharge = int(rentalPeriod) * float(dailyCharge)
elif rentalCode == "W":
    baseCharge = int(rentalPeriod) * float(weeklyCharge)

# Amount Due from Customer Variable:
amtDue = float(baseCharge) + float(mileCharge)

# Customer Rental Summary Output:
print("Rental Summary")
print("Rental Code: " + str(rentalCode))
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: " + "$%.2f" % amtDue)
'''END OF SCRIPT'''

/*
#################################################################
##       #       ##               ###     #######################
##       #       ##      #####     ##     #######################
##       #       ##      #####     ##     ######
##       #       ##               ###     ######
##       #       ##             #####     ##########
##       #       ##      ##      ####     ##########
##               ##      ##       ###     ######
##               ##      ###       ##     ######      ###
###             ###      ####       #     ######     #####
################################################      ###
*/




