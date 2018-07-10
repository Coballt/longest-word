
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        temporary_grid = self.grid.copy()
        if word == '':
            return False
        for letter in word:
            if letter in temporary_grid:
                temporary_grid.remove(letter)
            else:
                return False
        return True
