# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *

class myPlayer(PlayerInterface):
    """minmax de profondeur x"""

    def minmax(self, depth):
        if self._board.is_game_over() or depth == 0:
            return - self._board.diff_stones_board()
        
        moves = self._board.legal_moves()
        move = None
        if self._board._nextPlayer == self._board._BLACK:
            w = 10000
            for i in range (len(moves)):
                self._board.push(moves[i])
                #w = min(w, myPlayer.minmax(self, depth-1))
                tmp = myPlayer.minmax(self, depth-1)
                if w > tmp:
                    w = tmp
                    move = moves[i]
                self._board.pop()
            return w, move
        elif self._board._nextPlayer == self._board._WHITE:
            w = -10000
            for i in range (len(moves)):
                self._board.push(moves[i])
                #w = max(w, myPlayer.minmax(self, depth-1))
                tmp = myPlayer.minmax(self, depth-1)
                if w < tmp:
                    w = tmp
                    move = moves[i]
                self._board.pop()
            return w, move

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "Alexandre depth x"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        #moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        #move = choice(moves)
        heuristique, move = myPlayer.minmax_init(self, 2)
        self._board.push(move)

        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        #print("My current board :")
        #self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")
