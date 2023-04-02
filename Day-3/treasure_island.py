import time

def printAnimation():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_______/
    *******************************************************************************
    --------------------------WELCOME TO THE TREASURE GAME-------------------------
    *******************************************************************************
    ''')

def printEndGame(type):

    reason = ""

    if type == "right":
        reason = '''
    You were walking down the path with loud heart-ticks 💓... and suddenly you fell into a snare hole 🕳️, 86 feet deep and no one heard you ever after 😢🪦...
        '''
    elif type == "swim":
        reason = '''
    You were swimming 🏊‍♀️ across the river... the water was cold! While you were advancing near the bank, a deadly alligator 🐊 came out the water and pulled you down the water, and nobody saw you there after! 😢🪦...
        '''
    
    elif type == "red_door":
        reason = '''
    As you advanced to open the red door 🚪, a big lump of flame released at instant and burnt 🔥 you down! 😢🪦
        '''
    
    elif type == "blue_door":
        reason = '''
    As you advanced to open the blue door 🚪, a very powerful beast 🧌👹 turned down on you and teared you apart! And, you were never seen anywhere again! 😢🪦
        '''

    elif type == "invalid":
        reason = '''
    Your response was unclear 😵 and non defined, so you went crazy and died a tragic death! 😒🪦
        '''

    print(reason)
    time.sleep(5)
    print("------------GAME OVER-------------")
    time.sleep(2)
    response = input("Restart the game? | [Y]es or [N]o: ")
    if response == "y":
        init_response = "y"
        return init_response
    else:
        quit()

        


# =============================================================

printAnimation()

time.sleep(5)

init_response = input("Can we start? | [Y]es or [N]o: ")

while init_response == "y" or init_response == "Y":
    print('''
Once upon a time you went on a voyage 🚢⚓ to find a really valuable treasure 💎💍. And the map landed you in a mysterious island 🏝️ setup by the owner of the treasure to make it hard for the people to obtain the fortune 🪙. Lucky for you! the steps 🪜 are pretty simple, but every step makes you take a decision! If you take a wrong step, it will cost your life 😵🪦, meaning you will be eliminated ❌!
    ''')
    time.sleep(5)
    print('''
You have arrived at a pathway which turns LEFT ⬅️ and RIGHT ➡️...
Which path would you choose?
Type "R" for Right and "L" for Left!
    ''')
    d1 = input(">>> ")
    time.sleep(2)

    if d1 == "L" or d1 == "l":
        print('''
You were walking on the muddy road 🛣️, and you can barely see your surroundings, as the area was covered by the thick fog 🌫️. But you can hear the sound of a river 🌊 flowing nearby... as you walk down the path, you encounter a river 🌊

Now, you can swim 🏊‍♂️ across the river or wait till the fog uncovers a bit to see what's next!

Type "S" for swim and "W" for wait!
        ''')
        d2 = input(">>> ")
        time.sleep(2)

        if d2 == "S" or d2 =="s":
            printEndGame('swim')

        elif d2 == "W" or d2 == "w":
            print('''
As you were waiting by the bank of the river, the fog had cleared up a bit, and a building 🏛️ was visible a direction! so, you went near the building and then to see, the building had three doors! Confused you... tried referring the map 🗺️, to your wonder the treasure is just marked inside the building 🏛️. And there are 3 possible ways to enter the building! 
1. Go through the RED 🎟️  door.
2. Go through the BLUE 🟦 door.
3. Go through the YELLOW 🟡 door.
Type the number stated above in the instructions!
            ''')
            d3 = input(">>> ")
            time.sleep(2)

            if d3 == "1":
                printEndGame('red_door')
            elif d3 == "2":
                printEndGame('blue_door')
            elif d3 == "3":
                print('''
You went inside the door, and saw the treasure💍💎🪙! You won the the game!! 🎊🎉
                ''')
                time.sleep(5)
                # exiting the game
                init_response = "n"
            else:
                printEndGame('invalid')
        else:
            printEndGame('invalid')
            
    elif d1 == "R" or d1 == "r":
        printEndGame('right')
    
    else:
        printEndGame('invalid')

else:
    time.sleep(2)
    print("See you again! Bye!!")
    init_response = "n"
