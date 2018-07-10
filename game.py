
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

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
        return Game.__is_dict_word(word)

    @staticmethod
    def __is_dict_word(word):
        requ = requests.get('https://wagon-dictionary.herokuapp.com/'+word)
        return requ.json()['found']
