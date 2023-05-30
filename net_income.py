# Item names and earnings
earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

staff_expenses = {
    "Cleaner": 850,
    "Vendor": 1120,
    "Manager": 1330,
    "Loader": 900,
}

other_expenses = {
    "Electricity": 100,
    "Municipal service": 90,
    "Security": 30,
}

# Print item names and earnings
print("Earned amount:")
for item, earning in earnings.items():
    print(f"{item}: ${earning}")

# Calculate total earnings
total_earnings = sum(earnings.values())

# Print total earnings
print("\nIncome: $" + str(total_earnings))

# Print "Staff expenses" line
print("Staff expenses:")

# Ask for staff expenses
staff_expenses = float(input())

# Print "Other expenses" line
print("Other expenses:")

# Ask for other expenses
other_expenses = float(input())

# Calculate net income
net_income = total_earnings - staff_expenses - other_expenses

# Print net income
print("Net income: $" + str(net_income))
