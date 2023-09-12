# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# **7. Guess the Number:** - gave up....

import random


person_guess = 4
computer_pick = 10

def guess_number():
   pick = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
   person_guess = input("Choose a number from 1 - 10: ")
   computer_pick = random.choice(pick)
   guess = {"Your guess": person_guess, "Compuer's pick": computer_pick}

   return guess

guess = guess_number()
print(guess)
def check_num(person, computer):
   print(f"You guessed {person}, Computer chose {computer}")
   # if person == computer:
   #    print("Correct! :)")
   # elif person != computer:
   #    return "Incorrect guess"
      


#  **8. Hangman Game:** -- code not complete.. (also gave up..)
import random

word_list = ["hello", "school", "class", "cat", "bunny", "house", "penguin", "cherry", "warm", "sour"]

def choose_word():
    return random.choice(word_list)
# Not sure if this is all that goes here....

def display_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Hangman Game!")
    
    while True:
        print("Attempts left:", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ")

        if len(guess) != 1 
# ------------------

            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
            ------
    
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if set(word) == set(guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break

        if attempts == 0:
            print("\nGame over! The word was:", word)
            break
