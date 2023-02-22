# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *
from json import *
import buildOpenLibrary as bdl
from endGame import *

from openLibrary import *

class myPlayer(PlayerInterface):
    """minmax de profondeur x"""
    
    with open('openLibrary.json', 'r') as file: 
        _data = load(file)
    _opening_depth = bdl.nb_turn

    def MaxMin(self, depth): # ami
        if self._board.is_game_over() or depth == 0:
            return endGame.isEndGameBlack(self, depth)
        
        moves = self._board.legal_moves()
        best = -1000
        for move in moves:
            self._board.push(move)
            best = max(best, myPlayer.MinMax(self, depth-1))
            self._board.pop()
        return best


    def MinMax(self, depth): # adversaire
        if self._board.is_game_over() or depth == 0:
            return endGame.isEndGameBlack(self, depth)
        
        worst = 1000
        moves = self._board.legal_moves()
        for move in moves:
            self._board.push(move)
            worst = min(worst, myPlayer.MaxMin(self, depth-1))
            self._board.pop()
        return worst

    def best_move_minmax(self, depth):
        
        #if depth <= self._opening_depth: 
        #    opening_move = None
        #    for move in self._board.legal_moves(): 
        #        if move in self._data[depth - 1]:
        #            opening_move = move
        #            break
        #    if opening_move is not None:
        #        return opening_move
        
        opening_move = openLibrary.openingMove(self, depth);
        if opening_move is not None:
            return opening_move
        
        moves = self._board.legal_moves()
        best_move = []
        best = -100

        for move in moves:
            self._board.push(move)
            current_value = myPlayer.MaxMin(self, depth-1) 
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
        #moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        #move = choice(moves)
        move = myPlayer.best_move_minmax(self, 2)
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
