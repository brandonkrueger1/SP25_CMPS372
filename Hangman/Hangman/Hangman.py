import random

def hangman():
    word_lists = {
        "easy": ["cat", "dog", "bat", "tree", "fish"],
        "medium": ["mature", "printer", "computer", "dinosaur", "laptop"],
        "hard": ["certificate", "encryption", "framework", "debugging", "syntactical"]
    }

    # Corrected attempts based on difficulty
    difficulty_attempts = {
        "easy": 4,
        "medium": 6,
        "hard": 8
    }

    # Let user select difficulty
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower().strip()
    while difficulty not in word_lists:
        difficulty = input("Invalid choice. Please choose from easy, medium, or hard: ").lower().strip()

    word = random.choice(word_lists[difficulty]).lower()
    word_length = len(word)
    guessed_word = ['_'] * word_length
    guessed_letters = set()
    attempts = difficulty_attempts[difficulty]
    hint_shown = False

    print(f"\nWelcome to Hangman!")
    print(f"Difficulty Level: {difficulty.capitalize()}")
    print(f"The word has {word_length} letters.")

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Guess a letter or type 'hint': ").lower().strip()

        # Handle "hint" feature
        if guess == "hint":
            if not hint_shown:
                print(f"Hint: The first letter of the word is '{word[0]}'")
                hint_shown = True
            else:
                print("Hint has already been used.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try something else.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        if "_" not in guessed_word:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Main game loop
while True:
    hangman()
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print("Thanks for playing Hangman!")
        break