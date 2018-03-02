# -*-coding:Utf-8 -*

"""This file containing the main code of the game.

Execute it with Python for launche the game.

"""

import os
import pygame
from pygame.locals import *

from map import Map
from map import pick_the_map_from_txt

maze = pick_the_map_from_txt().maze

# Initialisation of the Pygame library
pygame.init()

pygame.mixer.music.load("music/hurry.mp3")
pygame.mixer.music.play()


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

if maze.won_the_game:
    pygame.mixer.music.stop()
    print("Felicitation !\nAvec l'ether, l'aiguille et la paille vous avez endormi le garde !\nYou won the game !")
if maze.loose_the_game:
    pygame.mixer.music.stop()
    print("Vous n'avez pas collecter l'ether, l'aiguille et la paille\npour endormir le garde.\nIl vous tue !")
