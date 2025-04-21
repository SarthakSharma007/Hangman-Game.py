import random  # Import random module to select a random word

# List of words to guess from
words = ["python", "hangman", "challenge", "programming", "computer", "science",
         "artificial", "intelligence", "machine", "learning", "data", "analysis",
         "statistics", "mathematics", "algorithm", "function", "variable", "loop",
         "condition", "array", "string"]

# Randomly choose a word from the list
chosen_word = random.choice(words)

# Create a display list with underscores (_) for each letter in the chosen word
word_display = ['_' for _ in (chosen_word)]

# Set the number of allowed incorrect attempts
attempts = 6

# Display welcome message
print("Welcome to the Game")

# Main game loop: runs while attempts remain and the word is not fully guessed
while attempts > 0 and '_' in word_display:
    # Show the current state of the guessed word
    print('\n' + ''.join(word_display))

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # If correct, reveal the guessed letter at its positions
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        print("Good Guess!")

    else:
        # If incorrect, decrease the number of attempts
        print("Wrong guess!")
        attempts -= 1

        # If no underscores remain, the player has won
        if '_' not in word_display:
            print("Congratulations! You've guessed the word:", chosen_word)
        # If no attempts left and word is not fully guessed
        else:
            print("Game over! The word was:", chosen_word)
            print("You Lost!")
