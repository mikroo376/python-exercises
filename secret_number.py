import random
def secret_number_user(min, max, limit):
    min_number = min
    max_number = max
    guess_count = 0
    guess_limit = limit

    random_number = random.randint(min_number,max_number)

    while guess_count != guess_limit:

        user_guess = int(input(f"Guess a number between {min_number} and {max_number}: "))
        guess_count += 1
        if user_guess == random_number:
            print("Bravo! You win!")
            break
        elif user_guess > random_number and guess_count != guess_limit:
            print(f"Sorry, guess again. Too high.")
        elif user_guess < random_number and guess_count != guess_limit:
            print(f"Sorry, guess again. Too low.")
        

    else: 
        print(f"Sorry you are out of gueses!\nThe hidden number was {random_number}")
secret_number_user(1,20,3)