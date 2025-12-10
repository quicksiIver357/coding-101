from random import random
from math import ceil

# other files
from difficulty_select import difficulty_select

# constants
EXIT = "exit"

def exit():
    if player_input.lower() == EXIT:
        print("Thanks for playing! Goodbye!")
        return True
    return False
def calculate_number():
    return ceil(random() * 100)
def generic_reset(games_played):
    input("Press Enter to play again...")
    number = calculate_number()  # Reset the number for a new game
    try_counter = 0
    games_played += 1
    return number, try_counter, games_played

number = calculate_number()
player_input = ""
first_time = True
try_cap = try_counter = wins = games_played = total_tries = 0 # set all stats to 0

running = True

# difficulty selection
try_cap = difficulty_select()

# main game loop
while running:
    # different prompt for first time
    if first_time:
        print("Welcome to the Number Guesser!")
        first_time = False

        player_input = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")

        # exit condition
        if exit():
            running = False
            break
    else:
        player_input = input()

    # validate input
    try:
        guessed_number = int(player_input)
        if guessed_number < 1 or guessed_number > 100:
            print("Please guess a integer within the range of 1 to 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a integer between 1 and 100.")
        continue

    # check guess
    if guessed_number < number:
        print("Too low! Try again.")
    elif guessed_number > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")
        number, try_counter, games_played = generic_reset(games_played)

        wins += 1
        continue

    # increment try counter / total_tries and check for max tries
    try_counter += 1
    total_tries += 1
    if try_counter >= try_cap:
        print(f"Sorry, you've used all your tries. The correct number was {number}.")
        number, try_counter, games_played = generic_reset(games_played)
        if exit():
            break

# final statistics
average_tries = total_tries / games_played if games_played > 0 else 0
win_rate = (wins / games_played * 100) if games_played > 0 else 0

print(f"""You played {games_played} game{"" if games_played == 1 else "s"} and won {wins} time{"" if wins == 1 else "s"}.
      Win rate: {win_rate}%
      Average tries per game: {average_tries} / {try_cap}""")

