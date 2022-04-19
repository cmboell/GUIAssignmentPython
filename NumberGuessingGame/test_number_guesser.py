"""
Program: guessing_game.py
Author: Colby Boell
Date: 04/18/2022

This program is used to create a GUI for a random number guessing game.
"""
import unittest
from NumberGuessingGame.guessing_game import NumberGuesser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.guessed_list = NumberGuesser([1, 9, 6])

    def tearDown(self):
        del self.guessed_list

    def test_constructor(self):
        self.assertEqual(self.guessed_list, [1, 9, 6])

    def test_add_guess(self):
        self.guessed_list = NumberGuesser([])
        self.guessed_list.add_guess(1)
        self.guessed_list.add_guess(9)
        self.guessed_list.add_guess(6)
        self.assertEqual(self.guessed_list, [1, 9, 6])


if __name__ == '__main__':
    unittest.main()
