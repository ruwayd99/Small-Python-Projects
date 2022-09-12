def display_board(board):
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-'*11)
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-'*11)
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('      ')
    
def player_input():
    
    choice = ''
    
    while choice.upper() not in ['X','O']:
        
        choice  = input('Player 1, are you X or O? ')
        
        if choice.upper() not in ['X','O']:
            
            print("That's a wrong input, dumbass.")
          
    if choice.upper() == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position-1] = marker

def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark: 
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark: 
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark: 
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark: 
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark: 
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark: 
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark: 
        return True

import random

def choose_first():
    
    if random.randint(1,10) <= 5:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position-1] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Pick the number corresponding to the box where you want your move to be '))
        if position not in range(1,10) or not space_check(board, position): 
            print('Try again dimbwit')
    return position

def replay():

    choose = 'Wrong'
    while choose.upper() not in ['Y','N']:    
        choose  = input('Continue playing? Y or N ')
        if choose.upper() not in ['Y','N']:
            print("That's a wrong input, dumbass.")
        if choose.upper() == 'Y':
            return True
        elif choose.upper() == 'N':
            return False
print('Welcome to Tic Tac Toe!')

while True:
    
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    
    first = choose_first()
    print(f'{first} will go first.')
    game_on = True
    
    ans = 'Wrong'
    while ans.upper() not in ['Y','N']:
        ans = input('Are you ready to play? Y or N ')
        if ans.upper() not in ['Y','N']:
            print("Maybe this game's not for you buddy. Try again though ")
    if ans.upper() == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        if first == 'Player 1':
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations player 1! You won the game.')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    first = 'Player 2'

        else:
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations player 2! You won the game.')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    first = 'Player 1'      
        
    if not replay():
        break
