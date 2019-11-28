"""
Board:

Create Shogi's board and set pieces
"""

class Board:

  # Creates the board, and places the pieces
  def create(self):
    board = [["*" for x in range(11)] for y in range(11)]

    # Replaces "*" with empty spaces for the actual board
    for i in range (1,10):
      for j in range (1,10):
        board[i][j]=" "

    # Adds row and col numbers in the top and left sides of the board
    for i in range(1,10):
      board[0][i] = i
    for i in range(1,10):
      board[i][0] = i

    # Adds the pieces for both players
    # Black pieces
    board[1][5] = "Kv"
    board[1][4] = "Gv"
    board[1][6] = "Gv"
    board[1][3] = "Sv"
    board[1][7] = "Sv"
    board[1][2] = "Nv"
    board[1][8] = "Nv"
    board[1][1] = "Lv"
    board[1][9] = "Lv"
    board[2][8] = "Bv"
    board[2][2] = "Rv"
    for i in range(1,10):
      board[3][i] = "Pv"

    # White pieces
    board[9][5] = "K^"
    board[9][4] = "G^"
    board[9][6] = "G^"
    board[9][3] = "S^"
    board[9][7] = "S^"
    board[9][2] = "N^"
    board[9][8] = "N^"
    board[9][1] = "L^"
    board[9][9] = "L^"
    board[8][2] = "B^"
    board[8][8] = "R^"
    for i in range(1,10):
      board[7][i] = "P^"

    return board
