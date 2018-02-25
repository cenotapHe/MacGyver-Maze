# -*-coding:Utf-8 -*

"""File containing the base of all obstacles."""

class Obstacle:

    """Class representing all obstacles.

    Obstacles are herited from this class. She
    defined further methods and attributs. 
    You need maybe to modified this methods or attributs
    in the class daughter.

    """

    name = "obstacle"
    can_cross = True
    symbol = ""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(nom=self.name,
                x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(nom=self.name, x=self.x, y=self.y)

    def arrive(self, maze, macgyver):
        """Method call when MacGyver arrive on the square.

        """
        pass
