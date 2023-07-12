# Hangman Game

This is a simple command-line Hangman game implemented in Python. The game randomly selects a word from a predefined word list and prompts the player to guess letters in order to uncover the word. The player has a limited number of lives, and they lose a life for each incorrect guess. The game ends when the player either guesses the word correctly or runs out of lives.

## File Organization

The code consists of three files:

1. `main.py`: This is the main script that runs the Hangman game. It imports the necessary modules and contains the game logic.
2. `hangman_art.py`: This module contains ASCII art used for visual representation of the Hangman stages as the player progresses through the game.
3. `hangman_words.py`: This module contains a list of words used by the game. The game randomly selects a word from this list for each round.

## Requirements

To run the Hangman game, you need to have Python installed on your system.

## How to Run

1. Make sure all three files (`main.py`, `hangman_art.py`, and `hangman_words.py`) are in the same directory.
2. Open a terminal or command prompt and navigate to the directory where the files are located.
3. Run the following command:

   ```shell
   python main.py
   ```

4. The game will start, and you will be prompted to enter your guesses.

## Gameplay

1. The game will display the Hangman ASCII art logo.
2. Enter your guess by typing a letter and pressing Enter.
3. If your guess is correct and the letter is present in the chosen word, the corresponding blank spaces will be filled in.
4. If your guess is incorrect and the letter is not in the chosen word, you will lose a life, and the Hangman ASCII art will progress to the next stage.
5. You cannot guess the same letter twice. If you try to guess a letter that you have already guessed, you will be notified.
6. The game continues until either you guess the word correctly (you win) or you run out of lives (you lose).
7. After the game ends, the final state of the Hangman ASCII art will be displayed, and you will be notified if you won or lost.

Enjoy playing Hangman!