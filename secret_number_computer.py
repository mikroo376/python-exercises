import random
def secret_number_computer(num):

    answer = ""
    min_guess = 1
    max_guess = num * 10
    while answer != "c":
        guess = random.randint(min_guess, max_guess)
        answer = input(f"Is {guess} too high(H), too low(L), or is it correct(C)?")
        if answer == "l":
            min_guess = guess + 1
        elif answer == "h":
            max_guess = guess - 1
        else:
            print("Incorrect letter!")

    else:
        print("Congratz! Computer wins!!!")

secret_number_computer(46)