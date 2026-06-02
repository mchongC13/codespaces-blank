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