import time
import Goban 
from random import choice
from playerInterface import *
from myPlayer import *
from json import *
import buildOpenLibrary as bdl


class openLibrary(PlayerInterface):
    
    def openingMove(self, depth):
        if depth <= self._opening_depth: 
            opening_move = None
        for move in self._board.legal_moves(): 
            if move in self._data[depth - 1]:
                opening_move = move
                break
        if opening_move is not None:
            return opening_move
