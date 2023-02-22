import time
import Goban 
from playerInterface import * 
from myPlayer import *
from json import *
import buildOpenLibrary as bdl

class openLibrary(PlayerInterface): 
    
    with open('openLibrary.json', 'r') as file: 
        _data = load(file)
    _opening_depth = bdl.nb_turn
        
    def openingMove(self, depth):
        if depth <= self._opening_depth: 
            opening_move = None
        for move in myPlayer._board.legal_moves(): 
            if move in self._data[depth - 1]:
                opening_move = move
                break
        return opening_move
