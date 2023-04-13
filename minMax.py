# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
minMax class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *
from endGame import *


class myPlayer(PlayerInterface):
    """minmax de profondeur x"""

    def MaxMin(self, depth, color, move): # ami
        if self._board.is_game_over() or depth == 0:
            return endGame.coloredHeuristique(self, depth, move, color)
        
        moves = self._board.legal_moves()
        best = -1000
        for move in moves:
            self._board.push(move)
            best = max(best, myPlayer.MinMax(self, depth-1, color, move))
            self._board.pop()
        return best


    def MinMax(self, depth, color, move): 
        if self._board.is_game_over() or depth == 0:
            return endGame.coloredHeuristique(self, depth, move, color)
        
        worst = 1000
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            worst = min(worst, myPlayer.MaxMin(self, depth-1, color, move))
            self._board.pop()
        return worst

    def best_move_minmax(self, depth, color):
        moves = self._board.legal_moves()
        best_move = []
        best = -1000

        for move in moves:
            self._board.push(move)
            current_value = myPlayer.MaxMin(self, depth-1, color, move)
            if best < current_value: 
                best = current_value
                best_move = [move]
            elif best == current_value:
                best_move.append(move)
            self._board.pop()
        return choice(best_move)

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "Alexandre depth 2"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        move = myPlayer.best_move_minmax(self, 2, self._mycolor)
        self._board.push(move)

        print("I am playing ", self._board.move_to_str(move))
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")