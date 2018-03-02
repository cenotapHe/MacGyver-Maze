# -*-coding:Utf-8 -*

"""This file containing the main code of the game.

Execute it with Python for launche the game.

"""

import os
import time
import pygame
from pygame.locals import *

from map import Map
from map import pick_the_map_from_txt

maze = pick_the_map_from_txt().maze

# Initialisation of the Pygame library
pygame.init()

pygame.mixer.music.load("music/hurry.mp3")
pygame.mixer.music.play()

maze.pygame()
pygame.display.flip()
time.sleep(5)


while not maze.won_the_game and not maze.loose_the_game:

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

    maze.pygame()
    pygame.display.flip()

if maze.won_the_game or maze.loose_the_game:
    pygame.mixer.music.stop()
    maze.end_of_the_game()
    pygame.display.flip()
    time.sleep(5)