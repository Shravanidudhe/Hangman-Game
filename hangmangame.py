import random

# List of words to choose from
words = ['python', 'developer', 'challenge', 'keyboard', 'function', 'algorithm', 'variable', 'condition', 'iteration']

# Function to choose a random word
def choose_word():
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to draw hangman
def draw_hangman(attempts):
    stages = [
        "  ----\n |    |\n |    O\n |   /|\\\n |   / \\\n_|_",
        "  ----\n |    |\n |    O\n |   /|\\\n |   / \
_|_",
 "  ----\n |    |\n |    O\n |   /|\\\n |
_|_",
        "  ----\n |    |\n |    O\n |   /|\
 |
_|_",
        "  ----\n |    |\n |    O\n |    |\
 |
_|_",
        "  ----\n |    |\n |    O\n |
 |
_|_",
        "  ----\n |    |\n |
 |
 |
_|_"
    ]
    print(stages[attempts])

# Main game function
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        draw_hangman(attempts)
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
            
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        draw_hangman(attempts)
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
