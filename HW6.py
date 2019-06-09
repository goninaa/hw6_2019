import numpy as np
import attr
# import enum
from enum import Enum

class Game:

    def __init__(self):
        self.board = np.zeros(4,5,3)
        

class Board (Enum):
    X = 4
    Y = 5
    Z = 3
    # def board (self):


if __name__ == "__main__":
    x, y, z = 2 ,6, 3
    # board = Board(x,y,3)
    board = Board(x,y)
    print (board.value)
