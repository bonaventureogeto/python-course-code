import random

secret_number = random.randint(1, 10)

attempts = 0

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10...")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a number!")
        continue
    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} tries")
        break
    elif guess < secret_number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again")
