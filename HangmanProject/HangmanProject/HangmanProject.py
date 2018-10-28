import random
import time
from os import name,system 
import sys
import tkinter
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("Hello World!!")

time.sleep(2)

name = input("Please Enter your name : " )



print("Welcome To Hangman ",name,"!!")

print('The rules are Simple you will be displayed an image and you have to guess what it is.')
print('Ready to play?')

gamechoice = input().upper()

if (gamechoice == 'Y' or gamechoice == 'YES'):
    print('Let\'s go then!! ' )
else:
    print('What a shame!')
    sys.exit()


words = {
    'apple'   :'"Images\apple.jpg"' ,
    'ironman' :'"Images\ironman.jpg"' ,
    'thor'    :'"Images\thor.jpg"', 
    'car'     :'"Images\car.jpg"',
    'clock'   :'"Images\clock.jpg',
    'football':'"Images\football.jpg'
    }


count = 3


for x in range(0,3):
    
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

gamechoice = input("Do you want to play any further?")

if (gamechoice == 'Y' or gamechoice == 'YES'):
    print('Let\'s go then!! ' )
else:
    print('Have a nice day')
    sys.exit()


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