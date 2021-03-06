import random
import sys
import time
from ttt.game import Game

def coin_flip():
    print('Who goes first?')
    # Make sure the player makes a valid guess
    while True:
        guess = input('Heads (H) or Tails (T): ').lower()
        if guess in ['heads', 'head', 'h', 'tails', 'tail', 't']:
            break
        print('Invalid input.')
    guess = guess[0]
    flip = random.choice(['h' ,'t'])

    # Print a nice flip animation
    states = ['_', '  \\', '    |', '     /', '      _', '      \\', '      |', '      /']
    print('Flipping...')
    for s in states:
        time.sleep(0.15)
        print('\t   ', s)
    if flip == 'h':
        print('\t      Heads!')
    else:
        print('\t      Tails!')
    time.sleep(0.5)
    print()

    # Player goes first if guess is correct
    return guess == flip

def main():
    try:
        # Check args for dimension argument
        board_size = int(sys.argv[sys.argv.index('-d') + 1])
    except:
        if len(sys.argv) > 1:
            print(f'USAGE: {sys.argv[0]} [-d <board size>]')
            sys.exit(0)
        board_size = 3

    # Decide who goes first
    player_turn = coin_flip()
    if player_turn:
        print('You are X')
    else:
        print('You are O')

    # Create new Game
    game = Game(player_turn, board_size)

    # Keep playing while game has not ended
    while not game.ended:
        game.print_board()
        # Make sure the player inputs a valid move:
        while True:
            try:
                move = int(input('Your turn! Play a space: '))
                if move < 0 or move >= len(game.board):
                    raise ValueError
                if game.board[move] == -1:
                    break
                print('You cannot choose a non-empty space.')
            except ValueError:
                print('Invalid index.')
        # Update game with chosen move
        game.player_turn(move)

    # Print game results
    print('\n--------------------------\n')
    print(game.result)
    game.print_board(print_indices=False)

if __name__ == '__main__':
    main()
