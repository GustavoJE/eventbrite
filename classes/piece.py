"""
Piece:

Contains methods that defines the possible movements of each piece type
"""

class Piece:

  def new_position_check(self):
    new_x, new_y = input("Input new coordinates: ").split()
    if int(new_x) >= 1 and int(new_x) < 10 and int(new_y) >= 1 and int(new_y) < 10:
      return [new_x, new_y]
    return "Out of bounds"

  def pawn_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if board[row][col] == "Pv":
      if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) == 1:
        board[int(new_positiony)][int(new_positionx)] = "Pv"
        board[row][col] = " "
      else:
        print("Invalid movement")
    elif board[row][col] == "P^":
      if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) == -1:
        board[int(new_positiony)][int(new_positionx)] = "P^"
        board[row][col] = " "
      else:
        print("Invalid movement")

  def lance_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if board[row][col] == "Lv":
      if (int(new_positionx)-col) == 0 and ((int(new_positiony)-row) <= 9 and (int(new_positiony)-row) > 0):
        board[int(new_positiony)][int(new_positionx)] = "Lv"
        board[row][col] = " "
      else:
        print("Invalid movement")
    elif board[row][col] == "L^":
      if (int(new_positionx)-col) == 0 and ((int(new_positiony)-row) >= -9 and (int(new_positiony)-row) < 0):
        board[int(new_positiony)][int(new_positionx)] = "L^"
        board[row][col] = " "
      else:
        print("Invalid movement")

  def knight_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if board[row][col] == "Nv":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1) and (int(new_positiony)-row) == 2:
        board[int(new_positiony)][int(new_positionx)] = "Nv"
        board[row][col] = " "
      else:
        print("Invalid movement")
    elif board[row][col] == "N^":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1) and (int(new_positiony)-row) == -2:
        board[int(new_positiony)][int(new_positionx)] = "N^"
        board[row][col] = " "
      else:
        print("Invalid movement")

  def rook_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if ((int(new_positionx)-col) <= 9 and (int(new_positiony)-row) == 0) \
      or ((int(new_positionx)-col) >= -9 and (int(new_positiony)-row) == 0) \
      or ((int(new_positionx)-col) == 0 and (int(new_positiony)-row) <= 9) \
      or ((int(new_positionx)-col) == 0 and (int(new_positiony)-row) >= -9):

      if board[row][col] == "Rv":
        board[int(new_positiony)][int(new_positionx)] = "Rv"
      else:
        board[int(new_positiony)][int(new_positionx)] = "R^"
      board[row][col] = " "
    else:
      print("Invalid movement")

  def bishop_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if int(new_positionx) == col or int(new_positiony) == row:
      print ("Invalid movement")
      pass
    elif (int(new_positionx)-col) <= 9 or (int(new_positionx)-col) >= -9 \
      and (int(new_positiony)-row) <= 9 and (int(new_positiony)-row) >= -9:
      if board[row][col] == "Bv":
        board[int(new_positiony)][int(new_positionx)] = "Bv"
      else:
        board[int(new_positiony)][int(new_positionx)] = "B^"
      board[row][col] = " "

  def king_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 \
      or (int(new_positionx)-col ==0)) and ((int(new_positiony)-row) == 1 \
      or (int(new_positiony)-row ) == -1 or (int(new_positiony)-row ) == 0):

      if board[row][col] == "Kv":
        board[int(new_positiony)][int(new_positionx)] = "Kv"
      else:
        board[int(new_positiony)][int(new_positionx)] = "K^"
      board[row][col] = " "
    else:
      print("Invalid movement")

  def gold_general_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if board[row][col] == "Gv":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 or (int(new_positionx)-col) == 0) \
        and ((int(new_positiony)-row) == 1 or (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) == 0) \
        and (int(new_positiony)-row == -1):
        board[int(new_positiony)][int(new_positionx)] = "Gv"
        board[row][col] = " "
      else:
        print("Invalid movement")
    elif board[row][col] == "G^":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 or (int(new_positionx)-col) == 0) \
        and ((int(new_positiony)-row) == -1 or (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) == 0) \
        and (int(new_positiony)-row == 1):
        board[int(new_positiony)][int(new_positionx)] = "G^"
        board[row][col] = " "
      else:
        print("Invalid movement")

  def silver_general_move(self, row, col, board):
    new_positionx, new_positiony = Piece().new_position_check()

    if board[row][col] == "Sv":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 or (int(new_positionx)-col) == 0) \
        and ((int(new_positiony)-row) == 1) or ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1) \
        and (int(new_positiony)-row == -1):
        board[int(new_positiony)][int(new_positionx)] = "Sv"
        board[row][col] = " "
      else:
        print("Invalid movement")
    elif board[row][col] == "S^":
      if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 or (int(new_positionx)-col) == 0) \
        and ((int(new_positiony)-row) == -1) or ((int(new_positionx)-col) == 1 (int(new_positionx)-col) == -1) \
        and (int(new_positiony)-row == 1):
        board[int(new_positiony)][int(new_positionx)] = "S^"
        board[row][col] = " "
      else:
        print("Invalid movement")
