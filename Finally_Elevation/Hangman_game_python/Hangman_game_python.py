import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer' , 'games' ,'teacher','student','school',
             'electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop','engineering',
             'hangman', 'circuit', 'imagination']

# Choose a random word
word = random.choice(word_list).lower()
guessed_letters = set()
correct_letters = set(word)
tries = 8


print("Welcome to Hangman!")
print("_ " * len(word))

# Game loop
while tries > 0 and correct_letters != guessed_letters:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        tries -= 1
        print(f"Wrong guess! You have {tries} tries left.")

    # Show current progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print(" ".join(display_word))

# Game result
if correct_letters == guessed_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
