import os
import random
import hangman_words as word
import hangman_art as art

chosen_word = random.choice(word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo + "Programmer Ver.")

display = ["_"] * word_length
not_in_word = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    if guess in display or guess in not_in_word:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        not_in_word += guess
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display or lives == 0:
        end_of_game = True
        if "_" not in display:
            print("You win.")
        else:
            print("You lose.")

    print(art.stages[lives])
