from questions import quiz
def quiz_game(play):
    if play.lower() == "yes":
        user_score = 0
        max_score = len(quiz)

        for question in quiz:
            user_answer = input(f"{question}: ")
            if user_answer.lower() == quiz.get(question).lower():
                print("Correct answer!")
                user_score += 1
            else :
                print("Incorrect answer!")

        print(f"You got {user_score} correct answers!\nYou got {user_score / max_score  * 100}%.")
    else:
        print("That's sad :( Bye bye")
        return

play = input("Welcome to my quiz game!\nDo you want to play? Yes or no: ")
quiz_game(play)