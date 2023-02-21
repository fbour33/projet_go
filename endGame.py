# -*- coding: utf-8 -*-

import time
import Goban 
from random import choice
import playerInterface

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

    # Cette fonction est adaptée pour le joueur blanc
    def isEndGameWhite(self, depth):
        nb = self._board.diff_stones_board()
        if self._board.is_game_over():
            if nb > 0:
                return lose
            elif nb < 0:
                return win
            else:
                return 0
        
        if depth == 0:
            return -nb

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

    def heuristique(self, depth, move): # pour le joueur BLACK
        difference = self._board.diff_stones_board()
        if self._board.is_game_over():
            if difference > 0:
                return lose
            elif difference < 0:
                return win
            else:
                return 0
        # la partie n'est pas finie, on va donc calculer l'heuristique
        nbBlack, nbWhite = endGame.neighbors(self, move)
        if depth == 0:
            return difference + nbBlack - nbWhite

move = "B1"

print(Goban.Board.name_to_flat(move))

move = "B2"
print(Goban.Board.name_to_flat(move))
print(Goban.Board.name_to_coord(move))