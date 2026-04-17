import random

words = ["python", "java", "react", "node", "mongo"]

word = random.choice(words)

guessed_letters = []
attempts = 5

print(" Welcome to Word Guessing Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("\n You Win! The word was:", word)
        break

# If user loses
if attempts == 0:
    print("\n Game Over! The word was:", word)