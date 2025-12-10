# difficulty constants
EASY = "easy"
MEDIUM = "medium"
HARD = "hard"
DEMON = "demon"


# function to handle difficulty selection
def difficulty_select():
    difficulty = input("Select difficulty (easy, medium, hard, demon): ").lower()

    if difficulty == EASY:
        return 20
    elif difficulty == MEDIUM:
        return 13
    elif difficulty == HARD:
        return 7
    elif difficulty == DEMON:
        return 4
    else:
        print("Invalid difficulty selected. Defaulting to medium.")
        return 13