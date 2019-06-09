import numpy as np
import attr
# import enum
from enum import Enum

class Game:
    """"""
    def __init__(self):
        self.board = np.zeros(4,5,3)

    def submarines (self, sub_num):
        pass
        

class Board:
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__z = 3
        self.board_shape = np.zeros ((self.x ,self.y, self.__z))

  


if __name__ == "__main__":
    x, y = 2 ,6
    board = Board(x,y)
    print (board.board_shape)
    # t = np.zeros ((4,5,3))
    # print (t)
  