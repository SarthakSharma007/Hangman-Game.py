# Hangman Game 🎮

Welcome to the classic **Hangman Game**, built using **Python**!  
Test your guessing skills by identifying hidden words — letter by letter — before you run out of attempts!

---

## 📜 Description

This is a simple text-based Hangman game where:
- A word is randomly selected from a predefined list.
- The player must guess letters to uncover the hidden word.
- Each incorrect guess reduces the number of remaining attempts.
- The game ends when the player either successfully guesses the entire word or runs out of attempts.

---

## ⚙️ How It Works

- A random word is selected at the start.
- The word is displayed as underscores (`_`) representing unguessed letters.
- The player inputs one letter per turn.
  - If the letter is correct, all instances of that letter are revealed.
  - If incorrect, the player loses one attempt.
- The player wins by guessing all letters correctly before running out of attempts.
- If all attempts are used without completing the word, the player loses and the correct word is displayed.

---

## 🛠️ Features

- Random word selection.
- Tracks and displays correct guesses.
- Limited number of wrong attempts (default: 6).
- Displays win or lose messages based on the outcome.
