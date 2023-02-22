# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
monteCarlo class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *
import numpy as np
from endGame import *
from openLibrary import *
class myPlayer(PlayerInterface):
    """Monte Carlo"""

    def best_move(moves, score, nb_simulation):
        best_moves = []
        max = score[0] / nb_simulation[0]
        for i in  range(len(moves)):
            if max < score[i] / nb_simulation[i]:
                max = score[i] / nb_simulation[i]
                best_moves = [moves[i]]
            elif max == score[i] / nb_simulation[i]:
                best_moves.append(moves[i])
        return choice(best_moves)

    def monteCarlo(self, depth):
        if self._board.is_game_over() or depth == 0:
            return endGame.isEndGameBlack(self, depth)

        opening_move = openLibrary.openingMove(self, depth)
        if opening_move is not None:
            return opening_move

        moves = self._board.legal_moves()
        score = np.zeros(len(moves))
        nb_simulation = np.zeros(len(moves))
        for i in range(len(moves)):
            self._board.push(moves[i])
            score[i] += myPlayer.monteCarlo(self, depth -1)
            self._board.pop()
            nb_simulation[i] += 1
        return myPlayer.best_move(moves, score, nb_simulation)
    


    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "MonteCarlo"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        #moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        #move = choice(moves)
        move = myPlayer.monteCarlo(self, 2)
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
