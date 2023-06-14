import random 
import time
number=random.randint(1, 50) 
def intro():
    print("May I ask you for your name?")
    name=input() #asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 50")
    print("You will be given 6 chances")
    time.sleep(.5)
    print("Go ahead. Guess!")
    pick(name)

def pick(name):
    guessesTaken = 0
    while guessesTaken < 6: 
        time.sleep(.25)
        enter=input("Guess: ") 
        try: # It is used to check whether a number is given or not
            guess = int(enter)    
            if guessesTaken<6:
                if guess<=50 and guess>=1: 
                    guessesTaken=guessesTaken+1 
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                    if guess==number:
                            break 
            if guess>50 or guess<1: 
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 50")

        except: #if a number isn't entered
            print("I don't think that "+enter+" is a number. Sorry")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))
        
#main

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    print("Do you want to play again?")
    playagain=input()