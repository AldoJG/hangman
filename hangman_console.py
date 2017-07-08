from hangman import HangmanGame, GameOver, InvalidGuess


def print_gallows(tries: int):
    """Note that this function is based on a six incorrect guesses maximum game"""

    if tries == 6:
        print('  +------+ \n'
              '  |      | \n'
              '         | \n'
              '         | \n'
              '         | \n'
              '         | \n'
              '########### ')
    if tries == 5:
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              '         | \n'
              '         | \n'
              '         | \n'
              '########### ')
    if (tries == 4):
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              '  |      | \n'
              '         | \n'
              '         | \n'
              '########### ')
    if tries == 3:
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              ' /|      | \n'
              '         | \n'
              '         | \n'
              '########### ')
    if tries == 2:
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              ' /|\     | \n'
              '         | \n'
              '         | \n'
              '########### ')
    if tries == 1:
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              ' /|\     | \n'
              ' /       | \n'
              '         | \n'
              '########### ')
    if tries == 0:
        print('  +------+ \n'
              '  |      | \n'
              '  0      | \n'
              ' /|\     | \n'
              ' / \     | \n'
              '         | \n'
              '########### ')


def will_continue(option: str) -> bool:
    option = option.upper()
    return option == 'Y' or option == 'YES'


if __name__ == '__main__':
    hm = HangmanGame()
    print('  HANGMAN')

    while True:
        if hm.is_active_game():
            try:
                print_gallows(hm.get_tries())
                print(hm)
                hm.make_guess(input('Make your guess: '))
                print()
            except InvalidGuess as invalid:
                print('\n'+str(invalid))
        else:
            print_gallows(hm.get_tries())
            if hm.is_victory(): print('YOU DID IT!')
            else: print('GAME OVER')
            print('Word: '+repr(hm).replace('Hangman_Game(','').rstrip(')'))

            if will_continue(input('\nContinue? ')) is False: break
            print()
            hm.reset()
