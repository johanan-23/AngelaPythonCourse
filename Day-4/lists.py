# Coding excerise

# The data(names of the people who went to the restraunt) is given a string, but the names are seperated by commas and spaces. The program must convert the string into a list of strings, and print a random name from the list.

# Example Input: Angela, Ben, Jenny, Michael, Chloe

import random

names = "Angela, Ben, Jenny, Michael, Chloe"

name_list = [str(name) for name in names.split(", ")]

selection = random.choice(name_list) # This is how we fetch a element from the list randomly!

print(selection)

# Another method:

# Continued from 11th line...

choice = random.randint(0, len(name_list)-1) # Since the index start from 0, the length of the list, will not be the last element! 
print(name_list[choice])
