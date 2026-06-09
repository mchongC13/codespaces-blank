"""This is a lesson on dictionary in Python"""

#Pairing value to each key
student = {"name": "James", "age":"17", "year": "13"}
print(student["name"])

#Changing value to a key 
student["name"] = "Sebastian"
print(f"The name is: {student["name"]}")

#Adding value to a non-existing key
student["subject"] = ["Accounting", "Maths","English", "Physics"]
print(f"Subjects taken:{student['subject']}")

#indexing from a dictionary
print(student["subject"][3])

#delete value from a dictionary using pop
print(student.pop("year"))
print(student)

#Using delete to remove values
del student["subject"][1:3]
print(student)

"""Dictionary Practice. Barry's program"""

# Importing the random module for random fact
import random

# Dictionary of planets
planets = {"Mercury": ('1', 'rock planet'), "Venus": ('2', 'rock planet'), "Earth": ('3', 'rock planet'), "Mars": ('4', 'rock planet'), "Jupiter": ('5', 'gas giant'), "Saturn": ('6', 'gas giant'), "Uranus": ('7', 'gas giant'), "Neptune": ('8', 'gas giant')}

# Get user input 
user_question = input("Do you want to know about the planets in our solar system? (yes/no) ").lower()

# Loop to allow user to ask about multiple planets
while user_question == "yes":
    
    user_input = input("Enter the name of a planet: ").lower().capitalize()

    # Check if the planet is in the dictionary and provide a random fact
    if user_input in planets:
        planet_number, planet_type = planets[user_input]
        print(random.choice([f"{user_input} is planet number {planet_number}.", f"{user_input} is a {planet_type}."]))
    
    else:
        print("That is not a planet in our solar system.")
    
    # Ask the user if they want to know about another planet
    user_question = input("Do you want to know about another planet? (yes/no) ").lower()

"""Dictionaries practise - Artin's program"""
import random

solar = {
    'Mercury': '2', 'Venus': '7', 'Earth': '67', 'Mars': '66777',
        'Jupiter': '8', 'Saturn': '9', 'Uranus': '5', 'Neptune': '02'
        }

dumbu = str(input('enter a planet: ')).strip().capitalize()
#this is a comment
if dumbu in solar:
    print(f"\nFacts about {dumbu}:")
    for fact in solar[dumbu]:
        print(f"- {fact}")
else:
    print("Error: That planet is not in our dictionary. Please try again.")

# Extar 4 nerds 
planet_names = list(solar.keys())
random_planet = random.choice(planet_names)
print(f"random fact is {solar[random_planet]}")