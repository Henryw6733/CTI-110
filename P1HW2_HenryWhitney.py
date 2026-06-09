# Whitney Henry
# 06/09/2026
# P1HW2 - Travel Expenses
# This program calculates travel expenses and displays remaining budget.

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel Destination: ")
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
expenses = gas + hotel + food
remaining = budget - expenses

print()
print("------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", budget)

print()
print("Fuel: ", gas)
print("Accommodation: ", hotel)
print("Food: ", food)

print()
print("Remaining Balance: ", remaining)