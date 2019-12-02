import os
from classes.board import Board
from classes.piece import Piece

"""
Main program
"""

# Instantiate the board class
board = Board().create()

while True:

  # Clears the screen between loop iterations (linux only)
  os.system("clear")

  # Prints the board
  print("\n\n".join(["\t".join([str(cell) for cell in row]) for row in board]))

  # Asks for coordinates and prints the contents of the selected box
  col_s, row_s = input("Input coordinates (x y): ").split()
  col = int(col_s)
  row = int(row_s)

  print("Selected piece: {}".format(board[row][col]))
  if board[row][col] == " ":
    print("Empty box, please try again")

  # Checks movement of pawns
  elif board[row][col] == "Pv" or board[row][col] == "P^":
    pawn = Piece()
    pawn.pawn_move(row, col, board)

  # Checks movement of lancers
  elif board[row][col] == "Lv" or board[row][col] == "L^":
    lance = Piece()
    lance.lance_move(row, col, board)

  # Checks movement of knights
  elif board[row][col] == "Nv" or board[row][col] == "N^":
    knight = Piece()
    knight.knight_move(row, col, board)

  # Checks movement of rooks
  elif board[row][col] == "Rv" or board[row][col] == "R^" :
    rook = Piece()
    rook.rook_move(row, col, board)

  # Checks movement of bishops
  elif board[row][col] == "Bv" or board[row][col] == "B^" :
    bishop = Piece()
    bishop.bishop_move(row, col, board)

  # Checks movement of kings
  elif board[row][col] == "Kv" or board[row][col] == "K^" :
    king = Piece()
    king.king_move(row, col, board)

  # Checks movement of gold generals
  elif board[row][col] == "Gv" or board[row][col] == "G^" :
    gold_general = Piece()
    gold_general.gold_general_move(row, col, board)

  # Checks movement of silver generals
  elif board[row][col] == "Sv" or board[row][col] == "S^" :
    silver_general = Piece()
    silver_general.silver_general_move(row, col, board)
