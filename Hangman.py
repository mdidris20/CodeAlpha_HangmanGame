import random
import os

def hangman():

    # List of 5 predefined words
    words = ["eternal", "strawberry", "charmful", "purity", "pineapple", "muse", "freedom", "tranquility", "laughter",
             "whisper", "radiant", "blossom", "cherish", "devotion", "orange", "affection", "apple", "courage", "journey",
             "serenity", "joyful", "fantasy", "flourish", "whisperer", "peace", "spark", "mango", "radiance", "humble", "sunshine",
             "dream", "timeless", "plum", "melody", "breeze", "kindness", "poetic", "celestial", "glow", "destiny", "smile", "evergreen",
             "nurture", "divine", "wonderland", "whispering", "embrace", "vision", "simplicity", "thrive", "golden", "gentle",
             "courageously", "imagine", "graceful", "inspire", "precious", "harmony", "endless", "guava", "banana",
             "calm", "unity", "charm", "luminous", "joy", "belief", "hope", "kiwi", "peaceful", "nature", "faith", "magic", "wonder", "stillness",
               "affectionate", "sparkle", "bloom", "trust", "muse", "eternal"]

    # Choose a random word
    word = random.choice(words)
    gussed_letters = []

    # Create display version of word (underscores)
    logo = r"""
  _
 | |                                           
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
"""
    print(logo)
    print("""Select level:
1. Easy
2. Medium
3. Hard
          """)
    level = input("Enter level: ")

    if level == "1":
        attempts_left = 10
        print(f"\nYou have {attempts_left} incorrect guesses allowed.")

    if level == "2":
        attempts_left = 6
        print(f"\nYou have {attempts_left} incorrect guesses allowed.")

    if level == "3":
        attempts_left = 4
        print(f"\nYou have {attempts_left} incorrect guesses allowed.")

    display_word = ["_"] * len(word)

    # Main game loop
    while attempts_left > 0 and "_" in display_word:
        print("\nWord:"," ".join(display_word))
        print(f"Gussed letters: {', '.join(gussed_letters)}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) !=1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue

        if guess in gussed_letters:
            print("You already gussed that letter.")
            continue

        gussed_letters.append(guess)

        if guess in word:
            print("Good guess!")

            # Reveal guessed letter in display_word
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess

        else:
            print("Wrong guess!")
            attempts_left -= 1

    # Game over conditions
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nOut of guesses! The word was:", word)

hangman()

y_n = input("\nPlay again? (y/n): ")
if y_n in ["y","yes"]:
    os.system("cls")
    hangman()
else:
    exit()