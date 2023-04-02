import random 

integer = random.randint(1, 1000)  # returns a "pseudo-random" integer between 1 and 1000
print(integer)

random_float = random.random()  # returns a random floating point value between 0 and 1

# To modify the range of the .random operator, multiply it with an integer

rand_float = random_float * 4

print(rand_float)  # This will return a value between 0 and 4

print(random_float)  # This will return a value between 0 and 1
