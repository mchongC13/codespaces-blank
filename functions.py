"""This is a lesson on using functions in Python"""

#Start function with def, hello is the function name and name is the parameter/value
def hello(name):
    """Says hello using function - passing the value in as a parameter"""
    print(f"Kia ora,{name}")

hello(input("Please enter your name"))

#We can have multiple parameters and arguments
def hello(name, period, time):
    """Says hello using function - passing the value in as a parameter"""
    print(f"Kia ora,{name}. It is now period {period} and the time is {time}")

hello("Ms Chong","2","9:30")

#We can assign a variable or scope inside a function - we call this local scope
def number():
    """prints out the value of variable/local scope within the function"""
    x=10
    print(f"x is the value inside the function: {x}")

number()

#We can't print the value of x outside the function - it was a local scope
number()
print(number)

#We can use function to return values
def number():
    """prints out the value of variable/local scope within the function"""
    x=10
    return x

number1 = number() #creating a global scope
print(number1 + 2)

#Local and global scope
def total():
    """Totals up x and y, returns as a total"""
    x = 3
    y = 5
    return x + y

num = total()
print(f"The total is: {num}")