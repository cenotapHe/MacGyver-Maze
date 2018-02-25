# -*-coding:Utf-8 -*

"""This modul containing the class Map."""

from maze import create_maze_from_chain

class Map:

    """Item of transition between the txt file and the maze.

    The maze is created from the containt of file txt.

    """

    def __init__(self, chain):
        self.maze = create_maze_from_chain(chain)

