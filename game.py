import random

print('Welcome to Tic Tac Toe!')


def display_board(board):
    print('\n'*5) # Clear screen
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


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

player_input()


def place_marker(board, marker, position):
    '''
    Take in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) 
    and assigns it to the board
    '''
    board[position] = marker

test_board
place_marker(test_board,'$',8)
display_board(test_board)


def choose_first():
    '''
    Randomly decide which player goes first
    '''
    flip = random.randit(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    '''
     Return a boolean indicating if a space is available
     '''
    return board[position] == ''


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