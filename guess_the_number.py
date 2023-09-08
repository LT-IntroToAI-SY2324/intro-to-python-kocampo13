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
   if person == computer:
      print("Correct! :)")
   elif person == 
      
