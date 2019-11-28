class Board:

    #creates the board, and places the pieces
    def create(self):    
        board = [["*" for x in range(11)] for y in range(11)]

        #replaces "*" with empty spaces for the actual board
        for i in range (1,10):
            for j in range (1,10):
                board[i][j]=" "

        #adds row and col numbers in the top and left sides of the board
        for i in range(1,10):   
            board[0][i] = i
        for i in range(1,10):
            board[i][0] = i

        #adds the pieces for both players
        #black pieces
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

        #white pieces
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
        if ((int(new_positionx)-col) <= 9 and (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) >= -9 \
            and (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) == 0 and (int(new_positiony)-row) <= 9) \
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
        elif (int(new_positionx)-col) <= 9 or (int(new_positionx)-col) >= -9 and (int(new_positiony)-row) <= 9 \
            and (int(new_positiony)-row) >= -9:
            if board[row][col] == "Bv": 
                board[int(new_positiony)][int(new_positionx)] = "Bv"
            else:
                board[int(new_positiony)][int(new_positionx)] = "B^"
            board[row][col] = " "

    def king_move(self, row, col, board):
        new_positionx, new_positiony = Piece().new_position_check()
        if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 or (int(new_positionx)-col ==0)) \
            and ((int(new_positiony)-row) == 1 or (int(new_positiony)-row ) == -1 or (int(new_positiony)-row ) == 0):
            if board[row][col] == "Kv": 
                board[int(new_positiony)][int(new_positionx)] = "Kv"
            else:
                board[int(new_positiony)][int(new_positionx)] = "K^"
            board[row][col] = " "
        else:
            print("Invalid movement")


"""
Main program
"""

#instantiate the board class
board = Board().create()

"""
Loop
"""

while True:
    #prints the board
    print("\n\n".join(["\t".join([str(cell) for cell in row]) for row in board]))

    #asks for coordinates and prints the contents of the selected box  
    col_s, row_s = input("Input coordinates (x,y): ").split()
    col = int(col_s)
    row = int(row_s)
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
               
    else:
        print(board[row][col])