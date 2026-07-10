# Whitney Henry
# 07/10/2026
# P5Lab
# This program simulates a self-checkout machine by generating a random purchase total, accepting a cash payment, calculating the customer's change, and displaying the change in dollars, quarters, dimes, nickels, and pennies.

import random

def disperse_change(change_amount):

    change = round(change_amount * 100)

    if change == 0:
        print("No change")
    else:
        num_dollars = change // 100
        change = change - (num_dollars * 100)

        num_quarters = change // 25
        change = change - (num_quarters * 25)

        num_dimes = change // 10
        change = change - (num_dimes * 10)

        num_nickels = change // 5
        change = change - (num_nickels * 5)

        num_pennies = change

        if num_dollars > 0:
            if num_dollars == 1:
                print(f"{num_dollars} Dollar")
            else:
                print(f"{num_dollars} Dollars")

        if num_quarters > 0:
            if num_quarters == 1:
                print(f"{num_quarters} Quarter")
            else:
                print(f"{num_quarters} Quarters")

        if num_dimes > 0:
            if num_dimes == 1:
                print(f"{num_dimes} Dime")
            else:
                print(f"{num_dimes} Dimes")

        if num_nickels > 0:
            if num_nickels == 1:
                print(f"{num_nickels} Nickel")
            else:
                print(f"{num_nickels} Nickels")

        if num_pennies > 0:
            if num_pennies == 1:
                print(f"{num_pennies} Penny")
            else:
                print(f"{num_pennies} Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")   

    cash_paid = float(input("How much cash will you put in the self-checkout? "))

    change_owed = round(cash_paid - amount_owed, 2)
    print(f"Change is: ${change_owed:.2f}")

    print()

    disperse_change(change_owed)


main()