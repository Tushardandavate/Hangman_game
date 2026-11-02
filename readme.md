# 🎮 Hangman Game (Python)

## 📌 About the Project

Hangman is a simple command-line word-guessing game developed using Python. The computer randomly selects a word from a predefined list, and the player has to guess the word one letter at a time.

The player gets a limited number of attempts to guess the correct word. If the player guesses all the letters before running out of attempts, they win. Otherwise, the game ends and reveals the correct word.

## 🚀 Features

- Random word selection using Python's `random` module.
- Letter-by-letter word guessing.
- Displays correctly guessed letters.
- Limited attempts (8 chances).
- Tracks the player's progress.
- Displays win or lose messages.

## 🛠️ Technologies Used

- Python 3
- Random Module

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

## ⚙️ How to Run the Project

**Step 1: Clone the repository**

```bash
git clone <your-repository-link>
```

**Step 2: Navigate to the project directory**

```bash
cd Hangman-Game
```

**Step 3: Run the Python file**

```bash
python3 hangman.py
```

## 🎯 How to Play

1. Run the Python program.
2. The computer randomly selects a word.
3. Guess one letter at a time.
4. Correct guesses reveal the letter in its position.
5. Incorrect guesses reduce your remaining attempts.
6. You win if you guess the complete word within 8 attempts.
7. You lose if you run out of attempts.

## 📚 Python Concepts Used

- Variables and Data Types
- Lists and List Comprehension
- Random Module (`random.choice()`)
- While Loop
- For Loop
- Conditional Statements (`if-else`)
- String Methods (`lower()`, `join()`)
- `enumerate()` Function
- Membership Operator (`in`)

## 🔮 Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Prevent repeated letter guesses.
- Display previously guessed letters.
- Add a play-again option.
- Add a graphical user interface (GUI).

## 👨‍💻 Author

**Tushar Dandavate**

---

⭐ If you like this project, feel free to explore and improve it!