# -*-coding:Utf-8 -*

"""File containing the class Guard, the end of the game."""

from obstacle.obstacle import Obstacle

class Guard(Obstacle):

    """Class representing the guard in front of the maze issue.

    When MacGyver come on this square, the game is considering over.
    With the three items, MacGyver escape the maze.
    Without MacGyver died.

    """

    can_cross = True
    name = "guard"
    symbol = "G"

    def arrive(self, maze, macgyver):
        """MacGyver arrive on the issue.

        The game is won !

        """
        maze.won_the_game = True
