import random

secret_number = random.randint(1, 10)

print("Welcome to Number Guessing Game 🎮")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print(" Congrats! You guessed the correct number!")
        break
    elif guess < secret_number:
        print("Too low! Try again ")
    else:
        print("Too high! Try again ")