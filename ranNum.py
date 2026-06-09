"""This is a guess the number game. Python task 3.1"""
#This imports random
import random

#variables
lowest_number = 0
highest_number = lowest_number

while highest_number < lowest_number + 10:
    lowest_number = int(input("Enter the lower number: "))
    highest_number = int(input("Enter the higher number: "))

secret_number = random.randint(lowest_number, highest_number)
#print("Shhh", secret_number)

user_guess = lowest_number - 1
while user_guess < lowest_number or user_guess > highest_number:
    user_guess = int(input("Enter your guess: "))

if user_guess == secret_number:
    print("Congratulations! You got it!")
else:
    print("Sorry, but the answer was", secret_number)

"""THis program finds random numbers, adds them and finds the average. Python task 3.2"""
import random

total = 0
num_trials = 10

for i in range(num_trials):
    rand_num = random.randint(1, 100)
    print(f"{i + 1}: {rand_num}")
    total += rand_num

print("Total:", total)
print("Average:", total / num_trials)

