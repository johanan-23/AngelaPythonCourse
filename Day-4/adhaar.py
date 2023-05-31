import random
ans = input("Start the program? (y/n): ")
while ans == "y":
    lopn = []
    for i in range(10000000000000, 99999999999999):
        m = random.randint(10000000000000, 99999999999999)
        lopn.append(m)
        
    c = random.choice(lopn)
    print(c)
    lopn.remove(c)
    ans = input("Start the program again? (y/n): ")