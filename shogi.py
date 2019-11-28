import os
from classes.board import Board
from classes.piece import Piece


"""
Main program
"""


#instantiate the board class
board = Board().create()

"""
Loop
"""

while True:
    #clears the screen between loop iterations (linux only)
    os.system("clear")

    #prints the board
    print("\n\n".join(["\t".join([str(cell) for cell in row]) for row in board]))

    #asks for coordinates and prints the contents of the selected box  
    col_s, row_s = input("Input coordinates (x,y): ").split()
    col = int(col_s)
    row = int(row_s)
    print("Selected piece: {}".format(board[row][col]))
    if board[row][col] == " ": 
        print("Empty box, please try again")
        
    #Checks movement of pawns
    elif board[row][col] == "Pv" or board[row][col] == "P^":
        Piece().pawn_move(row, col, board)
       
    #Checks movement of lancers
    elif board[row][col] == "Lv" or board[row][col] == "L^":
        Piece().lance_move(row, col, board)

    #Checks movement of knights
    elif board[row][col] == "Nv" or board[row][col] == "N^":
        Piece().knight_move(row, col, board)

    #Checks movement of rooks
    elif board[row][col] == "Rv" or board[row][col] == "R^" :
        Piece().rook_move(row, col, board)

    #Checks movement of bishops
    elif board[row][col] == "Bv" or board[row][col] == "B^" :
        Piece().bishop_move(row, col, board)
        
    #Checks movement of kings
    elif board[row][col] == "Kv" or board[row][col] == "K^" :
        Piece().king_move(row, col, board)
    
    #Checks movement of gold generals
    elif board[row][col] == "Gv" or board[row][col] == "G^" :
        Piece().gold_general_move(row, col, board)

    #Checks movement of silver generals
    elif board[row][col] == "Sv" or board[row][col] == "S^" :
        Piece().silver_general_move(row, col, board)


               
   