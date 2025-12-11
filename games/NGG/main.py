from json import load, dump

# my own files
from welcome import welcome

def main():
    # THIS CODE COMES FIRST
    save_data = load(open('games/NGG/game data/save.json')) # load data into dictionary

    save_data["times played"] += 1 # this is how many times the player has run the game

    welcome(save_data["times played"]) # welcome the player with a custom message

    # game logic here
    # add rolling, questions, shop, etc.

    # THIS CODE COMES LAST
    # save the player data
    dump(save_data, open('games/NGG/game data/save.json', 'w'), indent=4)

# only run the game if the code is run directly, not imported by another file
if __name__ == "__main__":
    main()

