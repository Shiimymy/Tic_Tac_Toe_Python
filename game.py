import random

print('Welcome to Tic Tac Toe!')

def display_board(board):
    print('\n'*2) # Clear screen
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)


def player_input():
    '''
    Output = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input ('Player 1, choose X or O:').upper()
        
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 = 'X'
    
    return (player1,player2)

# player_input()


def place_marker(board, marker, position):
    '''
    Take in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) 
    and assigns it to the board
    '''
    board[position] = marker

# test_board
# place_marker(test_board,'$',8)
# display_board(test_board)


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# display_board(test_board)
# win_check(test_board,'X')


def choose_first():
    '''
    Randomly decide which player goes first
    '''
    flip = random.randrange(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    '''
     Return a boolean indicating if a space is available
     '''
    return board[position] == ' '


def full_board_check(board):
    '''
    Check if the board is full 
    and returns a boolean value
    '''
    for i in range(1,10):
        if space_check(board, i):
            return False
    #Board is full if we return True
    return True


def player_choice(board):
    '''
    Ask for a player's next position (as a number 1-9)
    and check if position is available 
    then return position
    '''
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9):'))
    
    return position


def replay():
    '''
    Ask the player if they want to play again
    '''
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# Code to run the game: 

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            ### PLAYER ONE TURN
            
            display_board(the_board)
            # Add an handling error in case player choose a non digit
            try:
                position = player_choice(the_board) # choose a position
            except:
                print("Make sure to have an available number between 1 and 9")
                print("The game has to restart")
                player_input()

            place_marker(the_board, player1_marker, position) # place the marker

            # Check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    break # game_on = False
                # Next player turn if no win or no tie
                else:
                    print('Next Player turn')
                    turn = 'Player 2'

        else:
            ### PLAYER TWO TURN
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break