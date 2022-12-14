
player1 = input("Enter Player 1 name : ").upper()
player2 = input("Enter Player 2 name : ").upper()
#Display the board
def display_board(board):
   
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
    test_board = ['#','1','2','3','4','5','6','7','8','9']



#Input from the players for the choice of X or O
def player_input():
    
    marker = ''

    
    
    while not (marker == 'X' or marker == 'O'):
        marker = input(player1 + " choose X or O for the game : ").upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



#Ask the player for the positon and replace it with string provided
def place_marker(board, marker, position):
    board[position] = marker


#to check if someone won
def win_check(board, mark):
    
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or #accross horizontal
            (board[4]==mark and board[5]==mark and board[6]==mark)  or  #accross h
            (board[7]==mark and board[8]==mark and board[9]==mark) or # accross h
            (board[1]==mark and board[4]==mark and board[7]==mark) or #accross vertical
            (board[2]==mark and board[5]==mark and board[8]==mark) or #accross v
            (board[3]==mark and board[6]==mark and board[9]==mark) or #accross v
            (board[1]==mark and board[5]==mark and board[9]==mark) or #diagonal 
            (board[3]==mark and board[5]==mark and board[7]==mark))   #diagonal




#to check the turn of the player
import random
def choose_first():


    if random.randint(0,1) == 0:
        return player2
    else:
        return player1



#to check if there is spaace on board
def space_check(board, position):
    
    return board[position] == ' '




#to check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


#to chech the players next move
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose your next position (0-9) :"))
        
    return position


#to ask the player if want to play again
def replay():
    
    return input(" Do you want to play again ? Enter Yes or No :  ").lower().startswith('y')




#Final interaction of all the functions for the game

print("Welcome To Tic Tac Toe !")

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+ " will go first.")
        
    play_game = input("Are you ready to play game ? YES OR NO: ")
    
     
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
        
          
    while game_on:
        if turn == player1:
            #player 1 turn
                
            display_board(theBoard)
            print(player1)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker,position)
            
                         
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(player1+ ' have won the game!')
                game_on = False
                
                       
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw")
                    break
                    
                else:
                    turn = player2
                        
        else:
            #player 2 turn
            display_board(theBoard)
            print(player2)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(player2+ ' have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player1

    if not replay():
        break
                      



    

