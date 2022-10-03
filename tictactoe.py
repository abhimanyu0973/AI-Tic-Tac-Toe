from asyncio.windows_events import NULL
from tabnanny import check
from numpy import Infinity


def clear():    # clears all the markers in the entire board
    board = ["dont mind me"," "," "," "," "," "," "," "," "," "]

def display(): #displays the board
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

def check_P1():  #checks if P1 has won
    if(board[1] == board[2] == board[3] == P1 or board[4] == board[5] == board[6] == P1 or board[7] == board[8] == board[9] == P1 or board[1] == board[4] == board[7] == P1 or board[2] == board[5] == board[8] == P1 or board[3] == board[6] == board[9] == P1 or board[1] == board[5] == board[9] == P1 or board[3] == board[5] == board[7] == P1):
        return True
def check_P2():  #checks if P2 has won
    if(board[1] == board[2] == board[3] == P2 or board[4] == board[5] == board[6] == P2 or board[7] == board[8] == board[9] == P2 or board[1] == board[4] == board[7] == P2 or board[2] == board[5] == board[8] == P2 or board[3] == board[6] == board[9] == P2 or board[1] == board[5] == board[9] == P2 or board[3] == board[5] == board[7] == P2):
        return True

def tie_check():  #checks if there is any space left in the board
    for stuff in board:
        if (stuff == " "):
            return False
            break

def mark_P1():   #asks P1 for position and the marks the given position on the board
    P1_position = 0
    while not (1<= int(P1_position) <= 9 and board[P1_position] == " "):
        P1_position = int(input("P1 select your position (1-9)."))
    board[P1_position] = P1
    

def mark_P2():  #asks P2 for position and the marks the given position on the board
    P2_position = 0
    while not (1<= int(P2_position) <= 9):
        P2_position = int(input("P2 select your position (1-9)."))
    board[P2_position] = P2

def check_winner(board):

    if(check_P1() == True):
        return -1
    if(check_P2() ==  True):
        return 1
    if(tie_check() != False):
        return 0
    
    return 100

def minimax(board, is_maximising):

    if(check_winner(board) != 100):
        return check_winner(board)
    
    if(is_maximising):
        best_score = -Infinity
        for i in range(1,10):
            if(board[i] == " "):
                board[i] = P2
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = Infinity
        for i in range(1,10):
            if(board[i] == " "):
                board[i] = P1
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

    


while True:  #Final loop
    board = ["dont mind me"," "," "," "," "," "," "," "," "," "]  #initialising the board
    print("\n\n\n\n\nNEW GAME\nTic Tac Toe !! ")              
    clear()                 #clearing all the elements from the board if any.
    P1 = "X" #<<<<<--------------P1 choose your marker here (X or O) (Default X)

    win_P1 = False           #initialising variables
    win_P2 = False           #These determine if P1 or P2 has won.
    
    if(P1 == "X"):
        P2 = "O"
    else:                    #assigns a marker for P2
        P2 = "X"
    
    game_on = True
    best_score = -Infinity
    while game_on:

        display()
        mark_P1()
        if(check_P1() == True):
            print("Human Wins")
            game_on = False
            break
        if(tie_check() != False):
            print("Tie")
            game_on = False
            break
        best_score = -Infinity
        best_move = 0
        for i in range(1,10):
            if(board[i] == " "):
                board[i] = P2
                score = minimax(board, False)
                board[i] = " "
                if(score > best_score):
                    best_score = score
                    best_move = i

        board[best_move] = "O"
        if(check_P2() == True):
            print("AI Wins")
            game_on = False
            break
        if(tie_check() != False):
            print("Tie")
            game_on = False
            break
