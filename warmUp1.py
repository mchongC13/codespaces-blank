"""This program tracks the spending of transactions."""

# Declaring Variables
balances = [200]
money = 200
value = -1
zero = 0

# While loop through money
while money > zero and value != zero:
    try:
        value = int(input("Enter the amount spent: "))
        money -= value
        if value != zero:
            balances.append(money)
    except ValueError:
        print("That is not a valid transaction.")

# Looping through list
print("My bank balances have been:")
for each_money in balances:
    print(each_money)


"""Alternative prog- Spending tracker."""

money = 200
spending = [];
while True:
    try:
        amount = int(input("Enter the amount spent: "))
        if (amount > 0):
            spending.append(money) # add current money to list
            money -= amount
        else:
            spending.append(money)
            break
        if money <= 0:
            spending.append(money)
            break
    except ValueError:
        print("That is not a valid transaction.")
print("My bank balances have been:")
for i in spending:
    print(i)