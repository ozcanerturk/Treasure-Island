print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You're at the crossroad, which direction do you want to go? "
                "Type \"Left\" or \"Right\".\n").lower()

if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. "
                    "Type \"Wait\" to wait for a boat.\n "
                    "Type \"Swim\" to swimm across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived at a house, you entered inside and there are 3 doors with different colours: red, blue and yellow. "
                        "Which door do you choose to go in?\n "
                        "Type \"Red\" to open the red door.\n "
                        "Type \"Blue\" to open the blue door.\n "
                        "Type \"Yellow\" to open the yellow door."
                        ).lower()
        if choice3 == "yellow":
            print("You win the game. Hooray!")
        elif choice3 == "red":
            print("You are burned by fire. Game Over.")
        elif choice3 =="blue":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You made a typo. Game Over.")
    else:
        print("You are attacked by a trout. Game Over.")
else:
    print("You fall into a hole, the game is over.")