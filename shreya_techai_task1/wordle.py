import random
from colorama import Fore, init

init(autoreset=True)  # Automatically reset colors after each print

class Invalid(Exception):
    """Raise when a word less than or more than 5 letters is entered"""
    pass

def get_feedback(guess, secret):
    result = ""
    for i in range(5):
        if guess[i] == secret[i]:
            result += f"{Fore.GREEN}{guess[i].upper()} "  # Green - correct position
        elif guess[i] in secret:
            result += f"{Fore.YELLOW}{guess[i].upper()} "  # Yellow - in word but wrong position
        else:
            result += f"{Fore.LIGHTBLACK_EX}{guess[i].upper()} "    # Gray - not in word
    return result

def get_valid_guess():
    while True:
        try:
            guess = input("Enter word: ").lower()
            if len(guess) != 5:
                raise Invalid("Word must be exactly 5 letters!")
            return guess
        except Invalid as e:
            print("Oops!", e)

def main():
    # Read words from words.txt
    with open("words.txt") as f:
        WORDS = [line.strip().lower() for line in f if len(line.strip()) == 5]

    secret = random.choice(WORDS)
    chances = 6

    print("Welcome to Wordle! Guess the 5-letter word")

    for t in range(chances):
        guess = get_valid_guess()
        feedback = get_feedback(guess, secret)
        
        print("Feedback:", feedback)

        if guess == secret:
            print("Lessgo! the word was:", secret)
            break
    else:
        print("Sorry.. the word was:", secret)

    print("Thanks for playing")

if __name__ == "__main__":
    main()
