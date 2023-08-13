#Write a python program  to play tic tac toe board game
#Define initial board state
board=[" ", " ", " ",
       " ", " ", " ",
       " ", " ", " "]
#Define a function to print the current board state
def print_board():
  print("-------------")
  print("|",board[0],"|",board[1],"|",board[2],"|")
  print("-------------")
  print("|",board[3],"|",board[4],"|",board[5],"|")
  print("-------------")
  print("|",board[6],"|",board[7],"|",board[8],"|")
  print("-------------")
  #Define a function to check if a player has won
def check_win(player):
  #Check rows
  for i in range(0,9,3):
    if board[i]==board[i+1]==board[i+2]==player:
      return True
  #Check columns
  for i in range(3):
    if board[i]==board[i+3]==board[i+6]==player:
      return True
  #Check diagonals
  if board[0]==board[4]==board[8]==player:
    return True
  if board[2]==board[4]==board[6]==player:
    return True
   #No Winner
  return False
#Define the main game loop
def play_game():
  print("Welcome to Tic-Tac-Toe!")
  print_board()
  player="X"
  while True:
    #Get input from  the current player
    move=int(input("Player"+player+",enter your move(1-9):"))-1
    #Check if the move is valid
    if board[move]==" ":
      board[move]=player
    else:
      print("Invalid move.Try again.")
      continue
    #Check if the current player has won
    if check_win(player):
     #  print_board()
      print("Congratulations! Player",player,"Wins!")
      break
    #Check if the board is full
    if " " not in board:
      #print_board()
      print("It's a tie !")
      break
    #Switch to the other player
    if player=="X":
      player="O"
    else:
      player="X"
    #print the updated board
    print_board()
#Start the game
play_game()