# -*-coding:Utf-8 -*

"""This modul containing the class Maze."""

import os
import pickle
import random

from obstacle.wall import Wall
from obstacle.guard import Guard
from obstacle.ether import Ether
from obstacle.needle import Needle
from obstacle.straw import Straw
from macgyver import MacGyver

import pygame
from pygame.locals import *


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
        self.fenetre = pygame.display.set_mode((600, 600))
        self.macgyver = macgyver
        self.grid = {}
        self.grid[macgyver.x, macgyver.y] = macgyver
        self.macgyver.x = macgyver.x
        self.macgyver.y = macgyver.y
        
        self.won_the_game = False
        self.loose_the_game = False
        self.own_ether = False
        self.own_needle = False
        self.own_straw = False

        for obstacle in obstacles:
            if (obstacle.x, obstacle.y) in self.grid:
                raise ValueError("the coordinated x={} y={} are already " \
                        "used in this grid".format(obstacle.x,
                        obstacle.y))

            if obstacle.x > self.limit_x or obstacle.y > self.limit_y:
                raise ValueError("the obstacle {} are coordinated too " \
                        "larges".format(obstacle))

            self.grid[obstacle.x, obstacle.y] = obstacle

        self.obstacles = obstacles
            

    def pygame(self):
        """Display all the element graphic in the pygame console.
        """

        self.fond = pygame.image.load("picture/background.jpg").convert()
        self.fenetre.blit(self.fond, (0, 0))

        for obstacle in self.obstacles:
            if obstacle.symbol == "G":
                self.guard_picture = pygame.image.load("picture/Gardien.png")
                self.fenetre.blit(self.guard_picture, (obstacle.x*40, obstacle.y*40 + 30))
            if obstacle.symbol == "X":
                self.wall_picture = pygame.image.load("picture/fire1.png")
                self.wall_picture2 = pygame.image.load("picture/fire2.png")
                self.wall_picture3 = pygame.image.load("picture/fire3.png")
                self.mur_final = random.choice([self.wall_picture, self.wall_picture2,self.wall_picture3])
                self.fenetre.blit(self.mur_final, (obstacle.x*40 - 15, obstacle.y*40 - 23))
                self.mur_final = random.choice([self.wall_picture, self.wall_picture2,self.wall_picture3])
                self.fenetre.blit(self.mur_final, (obstacle.x*40, obstacle.y*40 - 10))
            if obstacle.symbol == "E":
                self.ether_picture = pygame.image.load("picture/ether.png")
                self.fenetre.blit(self.ether_picture, (obstacle.x*40 + 10, obstacle.y*40))
            if obstacle.symbol == "N":
                self.needle_picture = pygame.image.load("picture/needle.png")
                self.fenetre.blit(self.needle_picture, (obstacle.x*40 + 10, obstacle.y*40))
            if obstacle.symbol == "S":
                self.straw_picture = pygame.image.load("picture/straw.png")
                self.fenetre.blit(self.straw_picture, (obstacle.x*40 + 10, obstacle.y*40))

        self.inventory = pygame.image.load("picture/inventory.png").convert()
        self.fenetre.blit(self.inventory, (467, 20))

        if self.own_ether == True :
            self.fenetre.blit(self.ether_picture, (482, 51))
        if self.own_needle == True :
            self.fenetre.blit(self.needle_picture, (512, 51))
        if self.own_straw == True :
            self.fenetre.blit(self.straw_picture, (547, 56))

        self.player = pygame.image.load("picture/MacGyver.png").convert_alpha()
        self.player_position = self.player.get_rect()
        self.player_position = self.player_position.move((self.macgyver.x*40, self.macgyver.y*40 - 20))
        self.fenetre.blit(self.player, self.player_position)

    
    def display(self):
        """Display the maze in a console.

        We take the limits for display the grid. The obstacles and
        MacGyver are display in using their attribut of class 'symbol'.
        
        Uses this method only for debug the game in the console.

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

        The direction need to be precised on a chain, "north",
        "east", "south", or "west".

        If MacGyver meet a impassable obstacle, he stops.

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
        "e": Ether,
        "n": Needle,
        "s": Straw
    }

    x = 0
    y = 0
    macgyver = None
    ether = False
    needle = False
    straw = False
    obstacles = []
    for letter in chain:
        if letter == "\n":
            x = 0
            y += 1
            continue
        elif letter == " ":
            if not ether:
                prob = random.randint(0, 50)
                if x == 12 and y == 11 :
                    prob = 50
                if prob == 50 :
                    classe = symbols["e"]
                    item = classe(x, y)
                    obstacles.append(item)
                    ether = True
            if not needle:
                prob = random.randint(0, 50)
                if x == 3 and y == 9 :
                    prob = 50
                if prob == 50 :
                    classe = symbols["n"]
                    item = classe(x, y)
                    obstacles.append(item)
                    needle = True
            if not straw:
                prob = random.randint(0, 50)
                if x == 2 and y == 12 :
                    prob = 50
                if prob == 50 :
                    classe = symbols["s"]
                    item = classe(x, y)
                    obstacles.append(item)
                    straw = True
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
