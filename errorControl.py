"""Cookie order program"""

#Making a variable
num_cookies = -1

#Checking cookie order
while num_cookies < 0:
    try:
        num_cookies = int(input("Please enter the number of cookies"))
    except ValueError:
        print("Please enter a numeric value of cookies")
        
