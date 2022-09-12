def ready_play():
    choice = ''
    while choice not in ['Y','N']:
        choice = input('Are you ready to play the game? Type Y or N ').upper()
        if choice not in ['Y','N']:
            print('Invalid response')
    return choice

def choose_obj():
    choice = ' '
    while choice not in ['ROCK', 'PAPER', 'SCISSOR']:
        choice = input('Are you rock, paper or scissor? Type your move ').upper()
        if choice not in ['ROCK', 'PAPER', 'SCISSOR']:
            print('Invalid response')  
    return choice

import random
def comp_choice():
    
    x= random.randint(0,2)
    
    if x == 0:
        return 'ROCK'
    elif x == 1:
        return 'PAPER'   
    else:
        return 'SCISSOR'
def who_won(user, comp):
    
    if user == comp:
        print("It's a draw!")
        return 'D'
    elif user == 'ROCK' and comp == 'SCISSOR':   
        print('You won this round!')
        return 'U'
    elif user == 'ROCK' and comp == 'PAPER':   
        print('Computer won this round!')
        return 'C'   
    elif user == 'PAPER' and comp == 'ROCK':   
        print('You won this round!')
        return 'U' 
    elif user == 'PAPER' and comp == 'SCISSOR':   
        print('Computer won this round!')
        return 'C'   
    elif user == 'SCISSOR' and comp == 'PAPER':   
        print('You won this round!')
        return 'U' 
    elif user == 'SCISSOR' and comp == 'ROCK':   
        print('Computer won this round!')
        return 'C'
    
def tally(user_points, comp_points):
    print(f'You have {user_points} in total.')
    print(f'Computer has {comp_points} in total.')
    if user_points > comp_points:
        print('You are in the lead!')
    elif user_points == comp_points:
        print('You guys are tied right now')
    else:
        print('Computer is in the lead.')
def continue_game():
    choice = ''
    while choice not in ['C','N', 'E']:
        choice = input('Do you want to conitunue the game (C), start a new game (N) or exit game(E)? Type C, N or E ').upper()
        if choice not in ['C','N', 'E']:
            print('Invalid response')
    return choice

print('Welcome to rock, paper, scissor!')

while True:
    
    user_points= 0
    comp_points  = 0
    
    z = ready_play()
    
    if z == 'Y':
        main_game = True
    else:
        main_game = False
        
    while main_game:
        
        user = choose_obj()
        comp = comp_choice()
        print(f'The computer chose {comp}')
        
        r = who_won(user, comp)
        
        if  r == 'U':
            user_points += 1
        elif r == 'C':
            comp_points += 1
        else:
            pass
        
        tally(user_points, comp_points)
        
        q = continue_game()
        
        if q == 'C':
            
            main_game = True
        
        elif q == 'N':
            
            break
            
        elif q == 'E':
            
            break

    if q == 'E':
        break   
