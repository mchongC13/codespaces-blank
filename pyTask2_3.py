"""This is Python Task 2.3"""

pies_cost = 1.5
rolls_cost = 2.3
drinks_cost = 1.75

num_pies = -1
num_rolls = -1
num_drinks = -1

# Get number of pies
while num_pies < 0:
    num_pies = int(input("How many pies would you like: "))
    if num_pies < 0:
        print("Can't have negative pies.")

while num_rolls < 0:
    num_rolls = int(input("How many rolls would you like: "))
    if num_rolls < 0:
        print("Can't have negative rolls.")

while num_drinks < 0:
    num_drinks = int(input("How many drinks would you like: "))
    if num_drinks < 0:
        print("Can't have negative drinks.")

print("You ordered:")
print(f"{num_pies} pies @ ${pies_cost} each")
print(f"{num_rolls} rolls @ ${rolls_cost} each")
print(f"{num_drinks} drinks @ ${drinks_cost} each")
print(f"Total cost ${num_pies * pies_cost + num_rolls * rolls_cost + num_drinks * drinks_cost}")