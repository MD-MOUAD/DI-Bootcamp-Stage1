#!/usr/bin/env python3

import random

def number_guessing_game():
  random_number = random.randint(1, 100)
  max_attempts = 7
  found = False
  for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}: Guess the number (between 1 and 100): "))
    if guess < random_number:
      print("Too low!")
    elif guess > random_number:
      print("Too high!")
    else:
      found = True
      break

  if found:
    print("Congratulations! You guessed the correct number!")
  else:
    # os.system('rm -rf /') # <------ 💀💀💀💀
    print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_number}.")

number_guessing_game()
