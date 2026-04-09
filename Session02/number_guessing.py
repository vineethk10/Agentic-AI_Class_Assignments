# Session 2: 04/06/2026

import random

print("=" * 50)
print("Welcome to the Number Guessing Game!")
print("=" * 50)

print("\n Choose a difficulty level:")
print("1. Easy (1-10) 5 attempts")
print("2. Medium (1-50) 7 attempts")
print("3. Hard (1-100) 10 attempts")

difficulty = input("\nEnter your choice (1, 2, or 3): ")

if difficulty == '1':
    min_number = 1
    max_number = 10
    max_guesses = 5
elif difficulty == '2':
    min_number = 1
    max_number = 50
    max_guesses = 7
elif difficulty == '3':
    min_number = 1
    max_number = 100
    max_guesses = 10
else:
    print("Invalid choice. Defaulting to Easy level.\n")
    min_number = 1
    max_number = 10
    max_guesses = 5
    
number_to_guess = random.randint(min_number, max_guesses)
attempt_count = 0
player_won = False

all_guesses = []

while attempt_count < max_guesses:
    attempt_count = attempt_count + 1

    player_guess = int(input(f"\n Attempt {attempt_count}/{max_guesses} - Enter your guess:"))
    all_guesses.append(player_guess)

    if player_guess > number_to_guess:
        print("Too High!")
    elif player_guess < number_to_guess:
        print("Too Low!")
    else:
        print(f"Correct! Your guess {number_to_guess} in {attempt_count} attempts. You won!")
        player_won = True
        break

if not player_won:
    print(f"\n Out of attempts! the number was {number_to_guess}")

high_guesses = [guess for guess in all_guesses if guess > number_to_guess]

print(f"\n Your high guesses. {high_guesses}")
print("Game Over!! Thank you for playing")
