# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from endGame import *
from playerInterface import *
import buildOpenLibrary as bdl
from json import *




class myPlayer(PlayerInterface):
    """Current player"""
    
    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None
        self._indexOpeningMove = 0
        with open('openLibrary.json', 'r') as file: 
            self._data = load(file)
            print(self._board.str_to_move(self._data[0][0]) in self._board.legal_moves())
        self._opening_depth = bdl.nb_turn
        self._opponent_move = 'A1'

    #debut du minmax
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

    def alphaBeta(self, depth, color): # ok pour le BLACK
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
    #fin alphaBeta

    # bibliothèque d'ouverture    

    def openingMove(self, depth):
        opening_move = None
        for move in self._data[depth]: 
            for legalMove in self._board.legal_moves():
                if legalMove == self._board.str_to_move(move):
                    opening_move = move
                    break   
        return self._board.str_to_move(opening_move)
    #fin bibliothèque d'ouverture
    
    def getPlayerName(self):
        return "Bertin Bour"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        if self._indexOpeningMove >= self._opening_depth:
            move = myPlayer.alphaBeta(self, 3, self._mycolor)
        else:
            opening_move = self.openingMove(self._indexOpeningMove)
            self._indexOpeningMove += 1
            if opening_move != None:
                move = opening_move
            else:
                move = myPlayer.alphaBeta(self, 3, self._mycolor)
        self._board.push(move)

        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        #print("My current board :")
        #self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        self._opponent_move = move
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
