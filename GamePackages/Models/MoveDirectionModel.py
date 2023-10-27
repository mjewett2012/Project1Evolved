# MoveDirectionModel.py
from enum import Enum

class MoveDirection(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    UP = 5
    DOWN = 6

    def __str__(self):
        if self == MoveDirection.NORTH:
            return "north"
        elif self == MoveDirection.SOUTH:
            return "south"
        elif self == MoveDirection.EAST:
            return "east"
        elif self == MoveDirection.WEST:
            return "west"
        elif self == MoveDirection.UP:
            return "up"
        elif self == MoveDirection.DOWN:
            return "down"
        else:
            return "unknown"

    @staticmethod
    def from_string(direction):
        if direction == "north":
            return MoveDirection.NORTH
        elif direction == "south":
            return MoveDirection.SOUTH
        elif direction == "east":
            return MoveDirection.EAST
        elif direction == "west":
            return MoveDirection.WEST
        elif direction == "up":
            return MoveDirection.UP
        elif direction == "down":
            return MoveDirection.DOWN
        else:
            return None