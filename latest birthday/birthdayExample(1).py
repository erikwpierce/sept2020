import json

# getting user input
userInput = input("Enter a name:")
print("userInput = " + userInput)

# read the birthday json file 
pathToFile = 'C:\\Users\\User\\Documents\\SJCC\\Python\\latest birthday\\birthday.json'

with open(pathToFile, 'r') as openfile:

    # Reading from json file
    birthdayJSON = json.load(openfile)


birthdayDictionary = {}

# loop json list of data and put each name into a dictionary
for record in birthdayJSON:

    # fetch name and birthday
    name = record["name"]
    birthday = record["birthday"]

    print("name = " + name)
    print("birthday = " + birthday)

    birthdayDictionary[name] = birthday


# to print a value in the dictionary, give it a string with the name
print("That person's birthday is: " + birthdayDictionary[userInput])

# Repeat input
name = input("Enter a name:")
print("name = " + name)
