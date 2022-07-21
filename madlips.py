# You can add your sentences to the list with underscore x3 "___" as place to the user phrase.
phrases_list = ["Basketball is the best ___ in the world!", "Bring your own ___ to my sasuage party!", "Sell me your ___ please, i want it soo bad."]
new_phrases = ""
for phrase in phrases_list:

    user_phrase = input(f"Enter phrase number {phrases_list.index(phrase) + 1}: ")
    new_phrases += phrase.replace("___", user_phrase) + "\n"

print(new_phrases)