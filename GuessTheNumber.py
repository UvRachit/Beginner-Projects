#This is the programme where you have to chose a number in which u have to find the number in betn 0 and the one u choose.

import random

YON = input("Do You Want To Guesss? \n")
if YON == "yes".lower():
    print("Lets Do It!! ")
else:
    print("Get Lost Monkey!! ")
    quit()

topno = input("What Do You Want Your Top Range Of Number Be? \n")

if topno.isdigit():
    topno = int(topno)
    random_number = random.randint(0,topno)

else:
    print("Enter A Number As In Integer ")
    quit()

guess = int(0)

while True:
    guess += 1
    user_guess = input("Make A Guess: ",) 

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter A Number As In Integer ")
        quit()
    
    random_number = random.randint(1,topno)

    if user_guess == random_number:
        print("You Are Correct!! ")
        break

    elif user_guess > random_number:
        print("Less ")
    else:
        print("More ")
    continue

print("You Guessed It In",guess,"Guesses")
