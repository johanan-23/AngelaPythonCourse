data  = input("Give us any data: ")

if type(data) == str:
    print("You gave a string!")

elif type(data) == int or type(data) == float:
    print("You gave a number!")