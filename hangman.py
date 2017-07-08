from random import randrange
from re import match

DICTIONARY = 'en_dict.txt'
HIDDEN = '_'
ACCEPTABLE = '^[A-Za-z]+$'
TRIES = 6


class GameOver(Exception):
    pass


class InvalidGuess(Exception):
    pass


class HangmanGame:
    def __init__(self, word=''):
        assert type(word) == str, \
            'Chosen word "{}" is type {}; word must be str'.format(word, str(type(word)).lstrip("<class '").rstrip("'>"))

        if word == '':
            self._word = self._random_word()
        else:
            assert match(ACCEPTABLE, word) is not None, \
                'Chosen word "{}" contains invalid characters'.format(word)
            self._word = self._word_corrector(word)

        self._hidden = [HIDDEN]*len(self)
        self._tries = TRIES
        self._invalid_guesses = set()
        self._guesses = set()

    def __repr__(self):
        return 'Hangman_Game('+self._word+')'

    def __str__(self):
        output = ''
        for character in self._hidden: output += character+' '
        return output.rstrip()

    def __len__(self):
        return len(self._word)

    def __contains__(self, item):
        return item in self._word

    def __eq__(self, other):
        return other == self._word

    def _random_word(self) -> str:
        """ Selects a random word from the given dictionary """
        words = open(DICTIONARY).readlines()
        return self._word_corrector(words[randrange(0, len(words))].strip('\n'))

    def _word_corrector(self, word: str) -> str:
        return word.upper()

    def _update_hidden(self, g: str):
        if len(g) == len(self):
            self._hidden = [letter for letter in g]
        else:
            for index in range(len(self)):
                if self._word[index] == g:
                    self._hidden[index] = g

    def get_tries(self):
        return self._tries

    def is_active_game(self) -> bool:
        return self._tries != 0 and HIDDEN in self._hidden

    def make_guess(self, g: str) -> bool:
        if not self.is_active_game(): raise GameOver
        g = self._word_corrector(g)

        if not(len(g) == 1 or len(g) == len(self)):
            raise InvalidGuess('Guess "{}" must be either one character or the length of the word'.format(g))
        if match(ACCEPTABLE, g) is None:
            raise InvalidGuess('Guess "{}" contains invalid characters'.format(g))
        if g in self._guesses:
            raise InvalidGuess('Guess "{}" already made'.format(g))

        self._guesses.add(g)

        if g == self or g in self:
            self._update_hidden(g)
            return True

        self._invalid_guesses.add(g)
        self._tries -= 1
        return False

    def is_victory(self) -> bool:
        return HIDDEN not in self._hidden

    def reset(self, word=''):
        self.__init__(word)
