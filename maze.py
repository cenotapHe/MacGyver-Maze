# -*-coding:Utf-8 -*

"""This modul containing the class Maze."""

import os
import pickle

from obstacle.wall import Wall
from obstacle.guard import Guard
from macgyver import MacGyver


class Maze:

    """Class representing the maze.

    The maze is a grid with many wall, MacGyver and the Guard.
    All of this obstacles are in predetermined position.

    For create the maze form a chain (situated in a txt file) 
    considered the function 'create_maze_from_chain'
    definited below the class.

    """

    limit_x = 15
    limit_y = 15

    def __init__(self, macgyver, obstacles):
        self.macgyver = macgyver
        self.grid = {}
        self.grid[macgyver.x, macgyver.y] = macgyver
        self.won_the_game = False
        for obstacle in obstacles:
            if (obstacle.x, obstacle.y) in self.grid:
                raise ValueError("the coordinated x={} y={} are already " \
                        "used in this grid".format(obstacle.x,
                        obstacle.y))

            if obstacle.x > self.limit_x or obstacle.y > self.limit_y:
                raise ValueError("the obstacle {} are coordinated too " \
                        "larges".format(obstacle))

            self.grid[obstacle.x, obstacle.y] = obstacle

    def display(self):
        """Display the maze in a console.

        We take the limits for display the grid. The obstacles and
        MacGyver are display in using their attribut of class 'symbol'.

        """
        y = 0
        grid = ""

        while y < self.limit_y:
            x = 0
            while x < self.limit_x:
                square = self.grid.get((x, y))
                if square:
                    grid += square.symbol
                else:
                    grid += " "

                x += 1

            grid += "\n"
            y += 1

        print(grid)


    def move_macgyver(self, direction):
        """Move MacGyver.

        The direction (FOR NOW) need to be precised on a chain, "north",
        "east", "south", or "west".

        If MacGyver met a impassable obstacle, he stop.

        """
        macgyver = self.macgyver
        coords = [macgyver.x, macgyver.y]
        if direction == "north":
            coords[1] -= 1
        elif direction == "east":
            coords[0] += 1
        elif direction == "south":
            coords[1] += 1
        elif direction == "west":
            coords[0] -= 1
        else:
            raise ValueError("direction {} unknow".format(direction))

        x, y = coords
        if x >= 0 and x < self.limit_x and y >= 0 and y < self.limit_y:
            # We try to move MacGyver
            # We verified if aren't obstacle in this place
            obstacle = self.grid.get((x, y))
            if obstacle is None or obstacle.can_cross:
                
                # We delete the last position of MacGyver
                del self.grid[macgyver.x, macgyver.y]

                # We put MacGyver at the new place
                self.grid[x, y] = macgyver
                macgyver.x = x
                macgyver.y = y
                self.display()

                # We call the method 'arrive' of obstacle, if it exist
                if obstacle:
                    obstacle.arrive(self, macgyver)


def create_maze_from_chain(chain):
    """Created a maze from a chain.

    The symbols are definited by correspondance here.

    """
    symbols = {
        "x": Wall,
        "m": MacGyver,
        "g": Guard,
    }

    x = 0
    y = 0
    macgyver = None
    obstacles = []
    for letter in chain:
        if letter == "\n":
            x = 0
            y += 1
            continue
        elif letter == " ":
            pass
        elif letter.lower() in symbols:
            classe = symbols[letter.lower()]
            item = classe(x, y)
            if type(item) is MacGyver:
                if macgyver:
                    raise ValueError("Only one MacGyver in the maze")

                macgyver = item
            else:
                obstacles.append(item)
        else:
            raise ValueError("symbol unknow {}".format(letter))

        x += 1

    maze = Maze(macgyver, obstacles)
    return maze
