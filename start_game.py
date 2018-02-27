# -*-coding:Utf-8 -*

"""This file containing the main code of the game.

Execute it with Python for launche the game.

"""

import os
import pygame
from pygame.locals import *

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

# Initialisation of the Pygame library
pygame.init()

# Now, display the map and allow to play at every tour
maze.display()


while not maze.won_the_game:

    maze.pygame()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                maze.move_macgyver("east")
            if event.key == K_LEFT:
                maze.move_macgyver("west")
            if event.key == K_UP:
                maze.move_macgyver("north")
            if event.key == K_DOWN:
                maze.move_macgyver("south")


if maze.won_the_game:
    print("Felicitation ! You won the game !")
