# In this programme you have to play and also try to win rock paper sissors agains the computer...

import random

YON = input("Do You Want To Play Rock Paper Sissors??? ")
if YON == "yes".lower():
    print ("Lets See Your Luck!! ")
else:
    print("Then Get Lost Monkey!! ")
    quit()

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissors Or Q To Quit ").lower()
    if user_input == "q":
        break
    
    elif user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_picks = options[random_number]
    print("Computer Picked", computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissor":
        print("You Win!! ")
        user_wins += 1


    elif user_input == "paper" and computer_picks == "rock":
        print("You Win!! ")
        user_wins += 1

    elif user_input == "scissor" and computer_picks == "paper":
        print("You Win!! ")
        user_wins += 1

    else:
        print("Computer Wins!! ")
        computer_wins += 1

print("User Won", user_wins,"Times")
print("Computer Won", computer_wins,"Times")
print("GoodBye!! ")
