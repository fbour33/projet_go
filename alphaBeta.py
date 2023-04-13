# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
alphaBeta class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *
from myPlayer import *
from endGame import *
#from openLibrary import *

class myPlayer(PlayerInterface):
    """minmax de profondeur x avec alpha beta"""
    
    with open('openLibrary.json', 'r') as file: 
        _data = load(file)
    _opening_depth = bdl.nb_turn

    def openingMove(self, depth):
        if depth <= self._opening_depth: 
            opening_move = None
        for move in self._board.legal_moves(): 
            if move in self._data[depth - 1]:
                opening_move = move
                break
        return opening_move
    


    def MaxValue(self, depth, alpha, beta, currentMove, color):
        if self._board.is_game_over() or depth == 0:
            return endGame.coloredHeuristique(self, depth, currentMove, color)
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            alpha = max(alpha, myPlayer.MinValue(self, depth-1, alpha, beta, move, color))
            self._board.pop()
            if alpha >= beta:
                return alpha
        return alpha


    def MinValue(self, depth, alpha, beta, currentMove, color):
        if self._board.is_game_over() or depth == 0:
            return endGame.coloredHeuristique(self, depth, currentMove, color)
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            beta = min(beta, myPlayer.MaxValue(self, depth-1, alpha, beta, move, color))
            self._board.pop()
            if alpha >= beta:
                return alpha
        return beta

    def alphaBeta(self, depth, color):
        moves = self._board.legal_moves()
        alpha = -10000
        beta = 10000
        best_move = []
        
        for move in moves:
            self._board.push(move)
            current_value = myPlayer.MinValue(self, depth-1, alpha, beta, move, color)
            self._board.pop()
            if current_value > alpha:
                alpha = current_value
                best_move = [move]
            elif alpha == current_value:
                best_move.append(move)
            if alpha >= beta:
                return choice(best_move)
        return choice(best_move)

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None
        self._opponent_move = 'A1'

    def getPlayerName(self):
        return "Alexandre alphaBeta 2"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        
        move = myPlayer.alphaBeta(self, 3, self._mycolor)
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
