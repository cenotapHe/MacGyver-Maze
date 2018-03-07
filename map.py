# -*-coding:Utf-8 -*

"""This modul containing the class Map."""

from maze import create_maze_from_chain
import os

class Map:

    """Item of transition between the txt file and the maze.

    The maze is created from the containt of file txt.

    """

    def __init__(self, chain):
        self.maze = create_maze_from_chain(chain)

def pick_the_map_from_txt():
	"""Import the new map from a file txt
	"""

	for file_name in os.listdir("map"):
	    if file_name.endswith(".txt"):
	        pathway = os.path.join("map", file_name)
	        with open(pathway, "r") as file:
	            containing = file.read()
	            try:
	                map = Map(containing)
	            except ValueError as err:
	                print("Error from the read of {} : {}.".format(pathway, str(err)))
	return map