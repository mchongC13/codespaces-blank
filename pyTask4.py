"""This is Py Task 4.1 - Left to a sentence"""
sentence = input("Enter a sentence: ")

print(sentence[:5])

"""Py Task 4.2"""
sentence = ""
while sentence == "":
    sentence = input("Enter a sentence: ")
    if sentence == "":
        print("You didn't enter anything!")

num_chars = -1
while num_chars <= 0 or num_chars > len(sentence):
    num_chars = int(input("How many characters from the left:  "))
    if num_chars <= 0 or num_chars > len(sentence):
        print(f"Must be greater than 0 and smaller than {len(sentence) + 1}")

print(sentence[:num_chars])

"""Py Task 4.3"""
# Initialise variables
sentence = ""
num_characters = 0
left_or_right = ""

# Repeat asking for a sentence until something is entered
while sentence == "":
    sentence = input("Enter a sentence: ")

# Repeat asking for the number of characters until is in a valid range (greater than 0
# and less than the length of the sentence)
while num_characters <= 0 or num_characters > len(sentence):
    num_characters = int(input("Enter the number of characters: "))
    if num_characters <= 0 or num_characters > len(sentence):
        print(f"Must be between 1 and {len(sentence)}")

# Keep asking for whether the string is to be from the left or right until they
# have either entered "left" or "right"
while left_or_right != "left" and left_or_right != "right":
#while left_or_right not in ["left", "right"]:
    # The .lower() on the end will change their input to lowercase letters
    left_or_right = input("From the left or right: ").lower()
    print()


if left_or_right == "left":
    # Print characters from left
    print(sentence[:num_characters])
else:
    # Print characters from right
    print(sentence[-num_characters:])