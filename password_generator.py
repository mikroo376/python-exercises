import sys
import random
import string
password = []
char_left = 0
def update_chars_left(num_of_chars):
    global char_left
    if num_of_chars < 0 or num_of_chars > char_left:
        print(f"Characters number out of scale 0 - {password_length}")
        sys.exit()
    else:
        char_left -= num_of_chars
        print(f"Characters left: {char_left}")

password_length = int(input("How long the password should be: "))

if password_length < 6:
    print("Password length must be at least 6 characters long! Please enter correct value: ")
    password_length = int(input("How long the password should be: "))

else:
    char_left = password_length

lowercase_letters_num = int(input("How many lowercase letters should be in the password? "))
update_chars_left(lowercase_letters_num)

uppercase_letters_num = int(input("How many uppercase letters should be in the password? "))
update_chars_left(uppercase_letters_num)

special_num = int(input("How many special signs should be in the password? "))
update_chars_left(special_num)

digits_num = int(input("How many digits should be in the password? "))
update_chars_left(digits_num)

if char_left > 0:
    print("Not every char were used. Password will be completed by lowercase letters.")
    lowercase_letters_num += char_left

print(f"""
Password length: {password_length}
Lowercase letters number: {lowercase_letters_num}
Uppercase letters number: {uppercase_letters_num}
Special characters number: {special_num}
Digits number: {digits_num}
""")

for i in range(password_length):
    if lowercase_letters_num > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters_num -= 1
    elif uppercase_letters_num > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters_num -= 1
    elif special_num > 0:
        password.append(random.choice(string.punctuation))
        special_num -= 1
    elif digits_num > 0:
        password.append(random.choice(string.digits))
        digits_num -= 1

random.shuffle(password)

print(f'Generated password: {"".join(password)}')

# TO DO:
# 1. Validation - check if user types only numbers instead of letters or special characters

