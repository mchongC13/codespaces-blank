"""this is a program on lists"""

#list with indexing - slicing
fruits = ["apple", "banana", "watermelon", "cherries", "kiwi"]
print(fruits[0]) #apple
print(fruits[-1]) #kiwi
print(fruits[:3]) #['apple', 'banana', 'watermelon']
print(fruits[:-1]) #['apple', 'banana', 'watermelon','cherries']
print(fruits[2:4]) #watermelon and cherries - stops before 4
print(fruits[0:4:2]) #apple and watermelon, 2 is the stride - so how many we jump [0::2]
print(fruits[::2]) #apple, watermelon, kiwi

#editing and item on the list
fruits[4] = "lemon"
print(fruits)

#adding to a list
fruits.append("pear")
print(fruits)

#extend can also be use to add items to a list
fruits.extend(["plum","dragon fruits", "orange"])
print(fruits)

#deleted one item - cherries
del(fruits[3])
print(fruits)

#deleted more than 1 item
del(fruits[1:3])
print(fruits)

#length of items
print(len(fruits))

#finding the index position of the item
print(fruits.count("lemon"))

#iterating through list
for i in fruits:
    if i == "watermelon":
        print("This is my favourite")
    else:
        print("The rest")

age = [12, 24, 68, 33, 72, 45, 8, 50, 60]
for x in age:
    if x >= 65:
        print("You can retire")
    else:
        print("You have years of working life ahead of you")