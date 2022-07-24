# Need update !!!
import random
from words import words

def hangman():
    word = random.choice(words).upper()
    if " " in word or "-" in word:
        word = random.choice(words).upper()
        hidden_word = "- " * len(word)
    word_letters = set(word)  
    correct_letters = set()
    used_letters = set()
    

    while len(word_letters) != len(correct_letters):

        user_letter_guess = input("Guess a letter: ")
        if user_letter_guess in word_letters:
            correct_letters.add(user_letter_guess)
            
                
        else:
            used_letters.add(user_letter_guess)

        print(f"You have used these letters: {' '.join(used_letters).upper()}")
        print(f"Current word: {hidden_word}")
    else:
        print(f"You win! The word was: {word}")
    return
# hangman()

w="alibaba"
new_w = "-" * len(w)
print(new_w)
for letter in w:
    print(new_w)
    index = w[1:].index("a")
    new_w = new_w[:index] + "a" + new_w[index+1:]
    print(new_w)
   
