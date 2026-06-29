"""This program checks how many smart students there are."""

# Declaring variables
smart_bound = 80
score = input("Enter a score, or type 'done' to exit: ")
single = 1
smart_li = []
done = "done"

# While loop for the scores
while score != done:
    try:
        if int(score) >= smart_bound:
            smart_li.append(int(score))
        else:
            pass
    except:
        print("Invalid score!")
    score = input("Enter a score, or type 'done' to exit: ")

# Checking for number of smart students
if len(smart_li) == single:
    print("This class has 1 smart student!")
else:
    print(f"This class has {len(smart_li)} smart students!")