# display row
def display_ro(row):
    print("This is the row : ")
    print('|' +row[1]+ '|' +row[2]+ '|' +row[3]+ '|' +row[4]+ '|') 
    
    
ro = ['#', '1', '2', '3', '4']
display_ro(ro)



#index position which is been replaced
def index_pos():
    pos = 'wrong'
    
    while pos not in ['1','2','3','4']:
        pos = input("Give The Position To Be Replaced with The string between (1-4) : ")
        
        if pos not in ['1','2','3','4']:
            print("Give Correct Input")
        
        
    return int(pos)
    
    
    
#to enter the  given string in the row
def str1(ro, position):
    
    string_1 = input("Give the string to be replaced with the number : ")
    
    ro[position] = string_1
    
    return ro
    
    
#to continue the game
def continue_game():
    reply = 'wrong'
    
    while reply not in ['Y','N']:
        reply = input("Do you want to continue the game ? Say Y or N :  ").upper()
        
        if reply not in ['Y','N']:
            print("Please state Y or N")
        
        
    if reply == 'Y':
        return True
    else:
        return False
        
        
#Finally interacting all the functions
game = True

while game:
    display_ro(ro)
    
    position = index_pos()
    
    ro = str1(ro, position)
    
    display_ro(ro)
    
    game = continue_game()        
