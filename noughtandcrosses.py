import numpy as np


# game state class that holds all board essential parameters
class GameState:
    def __init__(self, board, current_player, rounds, winner, status, current_round):
        self.rounds = rounds
        self.board = board
        self.current_player = current_player
        self.winner = winner
        self.status = status
        self.current_round = current_round


# initialize the board and different parameters such as first player , winner and board status
def init_game():
    while True:
        user_input = input('Which player should start the game:  ')
        if user_input == 'X' or user_input == 'O':
            break
        else:
            print('invalid player character please try again ')
            continue
    board = np.chararray((3, 3))
    board[:] = 'N'
    current_player = user_input
    rounds = 9
    r = 0
    winner = ''
    status = 'No winner'
    game = GameState(board, current_player, rounds, winner, status, r)
    return game


# ask input from user to enter their desired play move
def player_moves(game):
    # to play on a grid location simply select a number from 1 to 9 ')

    while True:
        print('Player ', game.current_player, ' turn\n')
        move = input("Enter which position to play :  ", )
        if len(move) != 2:
            print('your move is not valid chose another one')
            continue
        elif (ord(move[0]) > 99 or ord(move[0]) < 97) or (
                (((ord(move[1]) - ord('0')) > 2) or ((ord(move[1]) - ord('0')) < 0))):
            print('your move is not valid chose another one')
            continue
        else:
            break
    return move


# function which performs the move on board
def play_move(game_state):
    move = player_moves(game_state)
    position = ord(move[1]) - ord('0')
    if move[0] == 'a' and game_state.board[0, position] == b'N':
        game_state.board[0, position] = game_state.current_player
    elif move[0] == 'b' and game_state.board[1, position] == b'N':
        game_state.board[1, position] = game_state.current_player
    elif move[0] == 'c' and game_state.board[2, position] == b'N':
        game_state.board[2, position] = game_state.current_player
    else:
        print('you can not play on this position choose a different one\n')
        play_move(game_state)

    return


# arrays of winning combinations on board
def init_win_arrays():
    win_array = np.chararray(3, 1)
    win_array[:] = 'X'
    win_array1 = np.chararray(3, 1)
    win_array1[:] = 'O'
    return win_array, win_array1


# define a horizontal win on board
def horizontal_win(game):
    win_array, win_array1 = init_win_arrays()
    for i in range(game.board.shape[1]):
        if np.array_equal(game.board[i, :], win_array):
            game.winner = 'X'
            game.status = 'winner'
            break
        if np.array_equal(game.board[i, :], win_array1):
            game.winner = 'O'
            game.status = 'winner'
            break
    return


# define a vertical win on board
def vertical_win(game):
    win_array, win_array1 = init_win_arrays()
    for i in range(game.board.shape[0]):
        if np.array_equal(game.board[:, i], win_array):
            game.winner = 'X'
            game.status = 'winner'
            break
        if np.array_equal(game.board[:, i], win_array1):
            game.winner = 'O'
            game.status = 'winner'
            break
    return


# define diagonal win on a board
def diagonal_win(game):
    win_array, win_array1 = init_win_arrays()
    right_diagonal = np.array([game.board[0, 2], game.board[1, 1], game.board[2, 0]])
    left_diagonal = np.array([game.board[0, 0], game.board[1, 1], game.board[2, 2]])
    if np.array_equal(right_diagonal, win_array) or np.array_equal(left_diagonal, win_array):
        game.winner = 'X'
        game.status = 'winner'
    if np.array_equal(right_diagonal, win_array1) or np.array_equal(left_diagonal, win_array1):
        game.winner = 'O'
        game.status = 'winner'


# check game status and end game in case of winner or draw
def end_game(game):
    if game.status == 'winner':
        return True
    elif game.current_round >= 9:  # check if board is full but no player has won the game .
        return True

    return False


# global function that holds all the winning moves
def winning_move(game):
    horizontal_win(game)
    vertical_win(game)
    diagonal_win(game)
    return


def output_result(game):
    if game.status == 'winner':
        print('player : ', game.winner, ' won the game congrats !')
    else:
        print('The game was a draw. Better luck next time')


# display the board during the game at each round
def display_board(game):
    print(game.board[0, 0].decode('utf-8'), '  | ', game.board[0, 1].decode('utf-8'), ' | ',
          game.board[0, 2].decode('utf-8'))
    print('----|-----|---')
    print(game.board[1, 0].decode('utf-8'), '  | ', game.board[1, 1].decode('utf-8'), ' | ',
          game.board[1, 2].decode('utf-8'))
    print('----|-----|---')
    print(game.board[2, 0].decode('utf-8'), '  | ', game.board[2, 1].decode('utf-8'), ' | ',
          game.board[2, 2].decode('utf-8'))


# main logic of the game is performed from start of game to end
def game_logic(game):
    while game.current_round < game.rounds:
        play_move(game)
        winning_move(game)
        display_board(game)
        if end_game(game):
            break
        if game.current_player == 'O':
            game.current_player = 'X'
        else:
            game.current_player = 'O'
        game.current_round = game.current_round + 1
    output_result(game)


# program starts here
def main():
    while True:
        game = init_game()
        game_logic(game)
        while True:
            response = input('Run again yes or no ? ')
            if response in ('yes', 'no'):
                break
            print('Invalid answer')
        if response == 'yes':
            continue
        else:
            print('Goodbye ;)')
            break


main()
