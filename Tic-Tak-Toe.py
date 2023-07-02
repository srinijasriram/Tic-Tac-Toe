print("WELCOME TO TIC TAC TOE")
import random
board = [   "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
currentplayer = "X"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])  
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#taking player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-" :
        board[inp-1] = currentplayer
    else:
        print("oops player is already on the spot.")

# checking for win or tie
def checkhorizontle(board):
    global winner
    if board[0] == board[1] ==board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] ==board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] ==board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] ==board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] ==board[8] and board[2] != "-":
        winner = board[3]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] ==board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] ==board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("Game is a Tie!")
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkhorizontle(board) or checkrow(board):
        print(f"the winner is : {winner}")


#switching the player1


def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "0"  
    else:
        currentplayer ="X"

#computer
def computer(board):
    while currentplayer == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchplayer()

#checking again for win or tie
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchplayer()
    computer(board)
    checkWin()
    checkTie(board)
