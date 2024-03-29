#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import sys
import gui
from classes import GameSetting, Game


# debug mode evaluation, enabling some more printouts, enabling console
DEBUG = (True if '--debug' in sys.argv else False)


# todo am ende aufräumen und unbenutzte variablen aufräumen/löschen
# todo alles was nicht notwendig ist nicht als klassenvariabe machen
# todo ini/jsom file with highscores and last gamesetting selected


AVAILABLE_MODES = {
    'Beginner': GameSetting(rows=9, cols=9, bombs=10),
    'Intermediate': GameSetting(rows=16, cols=16, bombs=40),
    'Expert': GameSetting(rows=16, cols=30, bombs=99),
    'Custom': GameSetting(rows=None, cols=None, bombs=None)  # todo
}


class Minesweeper:
    """
    A game of Minesweeper, built in python only and tkinter gui framework
    class handles main entry point for game
    """

    possible_modes = {
        'Beginner': GameSetting(rows=9, cols=9, bombs=10),
        'Intermediate': GameSetting(rows=16, cols=16, bombs=40),
        'Expert': GameSetting(rows=16, cols=30, bombs=99),
        'Custom': GameSetting(rows=None, cols=None, bombs=None)
    }

    def __init__(self):

        self._mode = self.possible_modes['Intermediate']  # todo select this based on last chosen option from json/ini
        self._game = Game(possible_settings=self.possible_modes, chosen_setting=self._mode)
        self._gui = gui.MinesweeperGUI(self._game, self.create_new)
        self._gui.build_gui()

    def create_new(self, setting):
        """
        create gui, destroy old if existing
        :return:
        :rtype:
        """
        if setting != self._game.curr_setting:
            self._mode = setting
            self._game = Game(possible_settings=self.possible_modes, chosen_setting=self._mode)
            self._gui.destroy()
            self._gui = gui.MinesweeperGUI(self._game, self.create_new)
            self._gui.build_gui()


if __name__ == '__main__':

    if '--debug' in sys.argv:
        print("Starting game in DEBUG Mode:")

    mw = Minesweeper()

    print("Done ...")
