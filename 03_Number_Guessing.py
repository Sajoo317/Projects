# The program generates a random number (1-100), and the user guesses it. Provide hints ("Too high" or "Too low").
# •	Skills Used: Loops, conditionals, random module, try and except

import random
def guess_number():
  a = random.randint(1,100)
  total_guesses = 5

  print("Welcome to the Number Guessing Game!!!\n")
  print("I am thinking of a number between 1 and 100. You have 5 guesses.\n")

  while total_guesses > 0:
    print(f"You have {total_guesses} guesses left.\n")
    try:
      guess = int(input("Take a guess: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      continue
  
    if guess > a:
      print("Too High!")
    elif guess < a:
      print("Too Low!")
    else:
      print(f"You got it! Congratulations You WON!!! in ", 5 - total_guesses ,"tries.")
      return
    total_guesses -= 1
  print(f"You ran out of guesses. The correct number was {a}.")
guess_number()


# Without using try and except
import random

def number_guessing_game():
    """Plays a number guessing game with the user."""

    number = random.randint(1, 100)
    guesses_left = 7

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        
        # Get player's guess and validate it
        guess_str = input("Take a guess: ")
        if guess_str.isdigit(): # Check if input is a number
            guess = int(guess_str)
            if 1 <= guess <= 100:  # Check if guess is in range
                
                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {7 - guesses_left} tries.")
                    return

                guesses_left -= 1
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Invalid input. Please enter a number.")


    print(f"Sorry, you ran out of guesses. The number was {number}.")

# Start the game
number_guessing_game()
