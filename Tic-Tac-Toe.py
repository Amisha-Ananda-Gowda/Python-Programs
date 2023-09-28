board=[" "," "," ",
       " "," "," ",
       " "," "," "]


def printboard():
    print("-------------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------------")
def checkwin(player):
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]==player:
            return True
    for i in range(0,3):
        if board[1]==board[i+3]==board[i+6]==player:
            return True
    if board[0]==board[4]==board[8]==player:
        return True
    if  board[2]==board[4]==board[6]==player:
        return True
    return False
def playgame():
    print("Welcome")
    printboard()
    player="X"
    while True:
        move= int(input("Player"+player+"enter your move"))-1
        if board[move]==" ":
            board[move]=player
        else:
            print("Invalid")
            continue
        if checkwin(player):
            print("Congratulations!")
            break
        if " " not in board:
            print("Tie")
            break
        if player=="X":
            player="O"
        else:
            player="X"
            
        printboard()
        
playgame()

