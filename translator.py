# translator 
#samogloska  = r

def translator(phrase):
    translation = ""
    vowels = "aeiouy"
    for letter in phrase:
        if letter in vowels:
            translation += "r"
        else:
            translation += letter
    return translation

print(translator(input("Enter a phrase to translate: ")))