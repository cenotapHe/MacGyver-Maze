# -*-coding:Utf-8 -*

"""This file containing the main code of the game.

Execute it with Python for launche the game.

"""

import os

from map import Map

# We load the existing map
maps = []
for file_name in os.listdir("map"):
    if file_name.endswith(".txt"):
        pathway = os.path.join("map", file_name)
        with open(pathway, "r") as file:
            containing = file.read()
            try:
                map = Map(containing)
            except ValueError as err:
                print("Error from the read of {} : {}.".format(
                        pathway, str(err)))

maze = map.maze

# Now, display the map and allow to play at every tour
maze.display()
while not maze.won_the_game:
    coup = input("> ")
    if coup == "":
        continue
    elif coup.lower() == "q":
        # We quit the game
        break
    elif coup[0].lower() in "nseo":
        letter = coup[0].lower()
        if letter == "e":
            direction = "east"
        elif letter == "s":
            direction = "south"
        elif letter == "o":
            direction = "west"
        else:
            direction = "north"

        # We try to convert the move
        coup = coup[1:]
        if coup == "":
            number = 1
        else:
            try:
                number = int(coup)
            except ValueError:
                print("Invalid number : {}".format(coup))
                continue

        maze.move_macgyver(direction)
    else:
        print("Coups autorisés :")
        print("  Q pour quitter la partie en cours")
        print("  E pour déplacer MacGyver vers l'est")
        print("  S pour déplacer MacGyver vers le sud")
        print("  O pour déplacer MacGyver vers l'ouest")
        print("  N pour déplacer MacGyver vers le nord")


if maze.won_the_game:
    print("Felicitation ! You won the game !")
