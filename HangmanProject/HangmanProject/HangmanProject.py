import random
import time
from os import name,system 
import sys
import tkinter
import random


#this is for the destroying the entire screens object "still in beta phase though"
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#program starts form here
print("Hello World!!")

time.sleep(2)

#name input
name = input("Please Enter your name : " )

#this should be displayed on the screen to greet the player
print("Welcome To Hangman ",name,"!!")

#confirmation screen
print('The rules are Simple you will be displayed an image and you have to guess what it is.')
print('Ready to play? Y/N')

gamechoice = input().upper()

#display as a block
if (gamechoice == 'Y' or gamechoice == 'YES'):
    print('Let\'s go then!! ' )
else:
    print('What a shame!')
    sys.exit()

#This is the dictionary to handle all the paths and the object name    

words = {
    'apple'   :'"Images\apple.jpg"' ,
    'ironman' :'"Images\ironman.jpg"' ,
    'thor'    :'"Images\thor.jpg"', 
    'car'     :'"Images\car.jpg"',
    'clock'   :'"Images\clock.jpg',
    'football':'"Images\football.jpg'
    }

#declaration of our iteration variable
count = 3

#this is the gaming loop (will run thrice)
for x in range(0,3):
    
    key = list(words.keys())[x]             #Here I first convereted the dictionary to list and then used the indexing to fetch the element
    val = list(words.values())[x]           #same as above
    print(val)
    
    #loop inside the for to give player 3 chances to answer
    while(count > 0):
        guess = input("Enter the guess of what this item/ Person could be \n")
        if guess == key:
            print('You guessed it right!!')
            break
        else:
            print('Your guess is wrong!')
            print(f'You have {count -1} chances left')
            count -= 1

            #user has only three tries no matter how many he answered or in which level the player is
    if count == 0:
        print('Looks like you have used all of your tries !!')
        break

#asking the user if he/she wants to continue any further
gamechoice = input("Do you want to play any further?")

if (gamechoice == 'Y' or gamechoice == 'YES'):
    print('Let\'s go then!! ' )
else:
    print('Have a nice day')
    sys.exit()


#giving back the players three lives
count = 0

#here we access the next three images from our dictionary and use them
for x in range(3,6):
    
    key = list(words.keys())[x] 
    val = list(words.values())[x]
    print(val)
    
    while(count > 0):
        guess = input("Enter the guess of what this item/ Person could be \n")
        if guess == key:
            print('You guessed it right!!')
            break
        else:
            print('Your guess is wrong!')
            print(f'You have {count -1} chances left')
            count -= 1

    if count == 0:
        print('Looks like you have used all of your tries !!')
        break