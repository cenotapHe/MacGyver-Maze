# -*-coding:Utf-8 -*

"""File containing the class Guard, the end of the game. One of the three items for ending the game."""

from obstacle.obstacle import Obstacle

import pygame
from pygame.locals import *

# When MacGyver happens on this item,
# item comes on his inventory.
# And the item make a sound.

pygame.init()
son = pygame.mixer.Sound("music/bring.wav")

class Straw(Obstacle):

    """Class representing the Straw.

    When MacGyver come on this square, he picks this item on his inventory.

    """

    can_cross = True
    name = "straw"
    symbol = "S"

    def arrive(self, maze, macgyver):
        """MacGyver arrive on this square.

        And take the straw on this inventory,
        with a sound to signale it at the player.

        """
        maze.own_straw = True
        son.play()
        for obstacle in maze.obstacles:
            if obstacle.symbol == "S":
                maze.obstacles.remove(obstacle)
