# -*- coding: utf-8 -*-

import time
import Goban 
from random import choice
from playerInterface import *

win = 1000
lose = -1000

class endGame:
    # Cette fonction est adaptée pour le joueur noir
    def isEndGameBlack(self, depth):
        nb = self._board.diff_stones_board()
        if self._board.is_game_over():
            if nb > 0:
                return win
            elif nb < 0:
                return lose
            else:
                return 0
        
        elif depth == 0:
            return nb
        
    def isendGame(self, depth, color):
        if color == Goban.Board._BLACK:
            return endGame.isEndGameBlack(self, depth)
        else:
            return endGame.isEndGameBlack(self, depth)

    def neighbors(self, move):
        """Retourne un couple, le nombre de voisin noir et le nombre de voisin blanc"""
        black = 0
        white = 0
        x, y = Goban.Board.unflatten(move)
        neighbors = ((x+1, y), (x+1, y+1), (x+1, y-1), (x-1, y), (x-1, y-1), (x-1, y+1), (x, y+1), (x, y-1))
        tab = [Goban.Board.flatten(c) for c in neighbors if Goban.Board._isOnBoard(self, c[0], c[1])]
        for i in range(len(tab)):
            if tab[i] == Goban.Board._BLACK:
                black += 1
            elif tab[i] == Goban.Board._WHITE:
                white += 1
        return black, white

    def heuristique(self, depth, move):
        nb = self._board.diff_stones_board()
        if self._board.is_game_over():
            if nb > 0:
                return win
            elif nb < 0:
                return lose
            else:
                return 0

        #gérer le cas du PASS, des fois on passe pour rien, ça "règle" le pb ...
        if move == 'PASS':
            nb -= 10

        if self._opponent_move == 'PASS':
            scoreBlack, scoreWhite = self._board.compute_score()
            return 1000*(scoreBlack - scoreWhite)
        #la partie est sur le point de finir il ne reste que 10 coups ou moins
        if self._board._nbBLACK + self._board._nbWHITE > 60:
            scoreBlack, scoreWhite = self._board.compute_score()
            return 5*(scoreBlack - scoreWhite)
        # la partie n'est pas du tout finie, on va donc calculer l'heuristique
        nbBlack, nbWhite = endGame.neighbors(self, move)
        nbCaptured = self._board.diff_stones_captured() # Black - White
        if depth == 0:
            return 5*nb + 2*nbCaptured + nbBlack - nbWhite
        
    def coloredHeuristique(self, depth, move, color):
        if color == Goban.Board._BLACK:
            return endGame.heuristique(self, depth, move)
        else:
            return -endGame.heuristique(self, depth, move)