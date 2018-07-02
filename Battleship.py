#adapted from codecademy.com/courses/learn-python/lessons/battleship/exercises

from random import randint
#initialise the board
board = []
#make a 5x5 grid of "O"s - the starting state
for x in range(0, 5):
  board.append(["O"] * 5)
#remove commas
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)
#functions to generate random coordinates for the battleship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

#allow at most 4 turns to be taken
for turn in range(4):
    #print the current turn
  print "Turn", turn + 1
  #take the guess coordinates as input
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  #win condition
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
    #validation
  else:
    #detect incorrect input formats
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    #detect if the guessed coordinate has already been tried
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)
    #end game at 4 turns
    if turn == 3: print "Game Over"
