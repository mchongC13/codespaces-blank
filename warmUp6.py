"""Warm Up Task 6 - The Challenge"""
#Variables
exit = "Why?"
suffix = " should go home next."
names = []

while True:
        bet = input("Who is least likely to win? ")
        if bet == exit:
            break
        elif bet.isalpha():
            names.append(bet)
        else:
            continue
if names:
    worst = max(names, key=names.count)
    print(worst + suffix)


"""An alternative solution - from Carter"""
# Variables used
target = ''
highestVote = 0
listOfNames = []

# Constants used
emptyString = ''
exit = "Why?"
question = "Who is going home next? "

while target != exit:
    target = input(question)
    
    # Check if input is letters only and not empty
    if target.isalpha() and target != exit:
        listOfNames.append(target)  # Store the actual text string, not True/False
    elif target == emptyString:
        continue

# Find the most frequent name in the list
for name in listOfNames:
    # Use listOfNames.count(name) instead of name.count(listOfNames)
    vote = listOfNames.count(name) 
    if vote > highestVote:
        highestVote = vote
        elimTarget = name

# Only print if at least one valid name was entered
if listOfNames:
    printingElimTarget = f"{elimTarget} is unlikely to win."
    print(printingElimTarget)
