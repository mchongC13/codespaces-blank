"""This program tests the temperature of the porridge."""

# Declaring variables
temperature = 0
output_temp = []
lower_bound = 34
upper_bound = 42
end_bound = -1

# While loop tests for continuous input
while temperature != end_bound:
    # Try and except tests for invalid input
    try:
        temperature = float(input("Enter the temperature: "))
        if temperature > upper_bound:
            output_temp.append("too hot")
        elif temperature < lower_bound:
            output_temp.append("too cold")
        else:
            output_temp.append("just right")
    except:
        print("Invalid temperature.")

output_temp.pop()

# Looping through the temperature
for temp in output_temp:
    print(temp)
