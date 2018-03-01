# -*-coding:Utf-8 -*

"""File containing the class Ether. One of the three items for ending the game."""

from obstacle.obstacle import Obstacle

import pygame
from pygame.locals import *

# When MacGyver happens on this item,
# item comes on his inventory.
# And the item make a sound.

pygame.init()
son = pygame.mixer.Sound("music/bring.wav")

class Ether(Obstacle):

    """Class representing the Ether.

    When MacGyver come on this square, he picks this item on his inventory.

    """

    can_cross = True
    name = "ether"
    symbol = "E"
    

    def arrive(self, maze, macgyver):
        """MacGyver arrive on this square.

        And take the ether on this inventory,
        with a sound to signale it at the player.

        """
        maze.own_ether = True
        son.play()
        for obstacle in maze.obstacles:
            if obstacle.symbol == "E":
                maze.obstacles.remove(obstacle)
