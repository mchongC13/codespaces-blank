"""This program checks for the bag weights of chips."""

# Declaring variables
weight = -1
weight_list = []
lower_bound = 150
upper_bound = 160

while weight != 0:
    try:
        weight = int(input("Enter the bag weight: "))
        if weight != 0 and (weight < lower_bound or weight >= upper_bound):
            print("REDIRECT")
        else:
            weight_list.append(weight)
    except:
        print("That is not a valid weight.")

weight_list.pop()
if len(weight_list) == 0:
    print("No valid weights.")
else:
    print("Weights:")
    for weight_val in weight_list:
        print(weight_val)