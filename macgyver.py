# -*-coding:Utf-8 -*

"""This module containing the class MacGyver.

This isn't the file for launche the game
(=> start_game.py).

"""

class MacGyver:

    """Class representing MacGyver."""

    symbol = "M"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<MacGyver x={} y={}>".format(self.x, self.y)

    def __str__(self):
        return "MacGyver {}.{}".format(self.x, self.y)
