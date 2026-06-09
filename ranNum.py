"""This is a guess the number game."""
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
