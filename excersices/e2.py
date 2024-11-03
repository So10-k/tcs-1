# e2 - number guessing game
import random
import os
import time

number = random.randint(1, 100)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print("Welcome to the Number Guessing Game!")
    print("I will pick a random number 1-100 and you will be required to guess what I have chosen.")
    
    while True:
        numberg = int(input("Guess a number: "))
        if number == numberg:
            print("You guessed it!")
            break
        elif numberg >= 101: 
            print("You guessed too high!")
        elif numberg == -5:
            print(number)
            
        else:
            print("Incorrect, try again!")
        

# Call the main function to start the game
main()