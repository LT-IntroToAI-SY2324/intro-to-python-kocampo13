import random


person_guess = 4
computer_pick = 10

def guess_number():
   pick = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
   person_guess = 6
   computer_pick = random.choice(pick)
   guess = {"Your guess": person_guess, "Compuer's pick": computer_pick}

   return guess

guess = guess_number()
print(guess)
if person_guess == computer_pick:
   print("Correct!")

else:
   print("Incorrct guess. Try again")

