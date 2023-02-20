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
        if self._board.is_game_over():
            if self._board.diff_stones_board() > 0:
                return win
            elif self._board.diff_stones_board() < 0:
                return lose
            else:
                return 0
        
        elif depth == 0:
            return self._board.diff_stones_board()

    # Cette fonction est adaptée pour le joueur blanc
    def isEndGameWhite(self, depth):
        if self._board.is_game_over():
            if self._board.diff_stones_board() > 0:
                return lose
            elif self._board.diff_stones_board() < 0:
                return win
            else:
                return 0
        
        if depth == 0:
            return - self._board.diff_stones_board()