Welcome Hangman 

A simple console-based Hangman game written in Python.

This Hangman game randomly selects a word from a predefined list. 

The player must guess the word one letter at a time. The player has 6 
incorrect guesses before the game ends.

Random word selection from a list

Case-insensitive input handling

Duplicate guess checking

Basic input validation (only one letter allowed per guess)

Display of correct guesses and remaining attempts

Example word list 
word_list = ['python', 'hangman', 
'challenge', 'programming', 'developer', 'games', 'teacher', 'student' 'electricity', 
'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop', 'engineering', 'hangman', 'circuit', 
'imagination',]

The game hides the word with underscores (_).

The player guesses one letter at a time.

If the guess is correct, the letter is revealed in its position(s).

If incorrect, the number of remaining tries decreases.

The game ends when the player either guesses the full word or runs out of tries.

