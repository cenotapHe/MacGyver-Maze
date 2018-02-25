# -*-coding:Utf-8 -*

"""File containing the class Wall, an impassable obstacle."""

from obstacle.obstacle import Obstacle

class Wall(Obstacle):

    """Class representing a Wall, an impassable obstacle."""

    can_cross = False
    name = "wall"
    symbol = "X"
