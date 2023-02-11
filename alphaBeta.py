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
    """minmax de profondeur x avec alpha beta"""

    def MaxValue(self, depth, alpha, beta):
        if self._board.is_game_over() or depth == 0:
            return self._board.diff_stones_board()
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            alpha = max(alpha, myPlayer.MinValue(self, depth-1, alpha, beta))
            self._board.pop()
            if alpha >= beta:
                return alpha
        return alpha


    def MinValue(self, depth, alpha, beta):
        if self._board.is_game_over() or depth == 0:
            return self._board.diff_stones_board()
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            beta = min(beta, myPlayer.MaxValue(self, depth-1, alpha, beta))
            self._board.pop()
            if alpha >= beta:
                return alpha
        return beta

    def alphaBeta(self, depth):
        moves = self._board.legal_moves()
        alpha = -100
        beta = 100
        best_move = 0
        for move in moves:
            self._board.push(move)
            current_value = myPlayer.MinValue(self, depth-1, alpha, beta)
            self._board.pop()
            if current_value > alpha:
                alpha = current_value
                best_move = move
            if alpha >= beta:
                return best_move
        return best_move

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "Alexandre alphaBeta 2"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        #moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        #move = choice(moves)
        move = myPlayer.alphaBeta(self, 2)
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
