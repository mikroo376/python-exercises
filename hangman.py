import random
from words import words

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def choose_word(words):
    word = random.choice(words).upper()
    if " " in word or "-" in word:
        word = random.choice(words).upper()
    hidden_word = []
    for _ in word:
        hidden_word.append("-")
    return word, hidden_word

def hangman():
    word, hidden_word = choose_word(words)  # Secred word and hidden version of the word
    
    
    word_letters = set(word)    # Secret word letters in a set
    correct_letters = set()     # User correct letters in a set
    used_letters = set()        # User used, incorrect letters in a set


    

    while len(word_letters) != len(correct_letters):
        user_letter_guess = input("Guess a letter: ").upper()
        if user_letter_guess in word_letters:
            correct_letters.add(user_letter_guess)
            indexes = find_indexes(word, user_letter_guess) # Indexes of every correct letter in secret word
            for index in indexes:
                hidden_word[index] = user_letter_guess      # Replace hidden sign "-" with correct letter  
        else:
            used_letters.add(user_letter_guess)             # Add incorrect letter to used letters set
        # Display actual state of game to the user
        print(f"You have used these letters: {' '.join(used_letters).upper()}\nCurrent word: {' '.join(hidden_word)}")
    else:
        print(f"You win! The word was: {word}")
    return
hangman()

# TO DO:
# 1. Add validation / allow user to enter only single letter. Give 1 more chance to type correct letter.
# 2. At the end of the game ask user if he wants to play again.
# 3. If user wants to play again, make sure that secret word from game before doesn't appear in next games.
# 4. Add user lifes count and limit of lifes that user has / if user type same letter again life count doesnt decrease. 
# 5. Add difficulty level and ask user before game starts which level is he choosing (life count difference)
# 6*. Add "hint" feature for user when 3 lifes left. (words = dict / "Word":"Hint")
