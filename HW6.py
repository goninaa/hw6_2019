import numpy as np
import attr
# import enum
from enum import Enum

class Game:
    """"""
    def __init__(self):
        self.board = np.zeros(4,5,3)

    def submarines (self, sub_num):
        # horizontal:

        pass
        

class Board:
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deep = np.zeros((self.x,self.y), np.int8)
        self.sea_level = np.zeros((self.x,self.y), np.int8)
        self.air = np.zeros((self.x,self.y), np.int8)
        # self.__z = [Deep, Sea-level, Air]

    def submarines (self):
        
        sub_x = np.random.randint(self.x, size=1)[0]
        sub_y = np.random.randint(self.y, size=1)[0]
        print (sub_x, sub_y)
        try:
            # horizontal:
            self.deep[sub_x][sub_y]= 1
            self.deep[sub_x][sub_y+1]= 1
            self.deep[sub_x][sub_y+2]= 1
            # vertical:
            self.deep[sub_x][sub_y]= 1
            self.deep[sub_x+1][sub_y]= 1
            self.deep[sub_x+2][sub_y]= 1
        except IndexError:
            pass #fix this
        # self.deep[0][3]= 1
        # print (sub)
        
    def show (self):
        pass

  


if __name__ == "__main__":
    x, y = 2 ,6
    board = Board(x,y)
    print (board.deep)
    board.submarines()
    print (board.deep)
    # t = np.zeros ((4,5,3))
    # print (t)
    # sub = np.random.choice([0, 1], size=(10,), p=[1./3, 2./3])
    # np.random.randint(2, size=10)