


import random

words = ['python', 'java', 'javascript', 'ruby', 'kotlin', 'go', 'swift']

# Choose randomly
choose_word = random.choice(words)

word_Display = ['_' for _ in choose_word]

attempts = 8

print("Welcome to Hangman Game!")

while attempts > 0 and '_' in word_Display:

    print("\n" + ' '.join(word_Display)) 
    # join converts list into single string
    print("Remaining attempts:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in choose_word:

        for index, letter in enumerate(choose_word):

            if letter == guess:
                word_Display[index] = guess

    else:
        print("The letter does not appear in the word!")
        attempts -= 1

# Game conclusion

if '_' not in word_Display:

    print("\nYou guessed the word!")
    print(''.join(word_Display))
    print("You survived!")

else:

    print("\nYou ran out of attempts.")
    print("The correct word was:", choose_word)
    print("You lost!")
