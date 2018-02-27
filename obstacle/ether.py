# -*-coding:Utf-8 -*

"""File containing the class Guard, the end of the game."""

from obstacle.obstacle import Obstacle

import pygame
from pygame.locals import *

pygame.init()
son = pygame.mixer.Sound("music/bring.wav")

class Ether(Obstacle):

    """Class representing the guard in front of the maze issue.

    When MacGyver come on this square, the game is considering over.
    With the three items, MacGyver escape the maze.
    Without MacGyver died.

    """

    can_cross = True
    name = "ether"
    symbol = "E"
    

    def arrive(self, maze, macgyver):
        """MacGyver arrive on the issue.

        The game is won !

        """
        maze.own_ether = True
        son.play()
        for obstacle in maze.obstacles:
            if obstacle.symbol == "E":
                maze.obstacles.remove(obstacle)
