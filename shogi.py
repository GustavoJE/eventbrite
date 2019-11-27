from helpers import helpers

"""
Initialization of the shogi board
"""

board = helpers.board_create()

while True:
    #prints the board
    print("\n\n".join(["\t".join([str(cell) for cell in row]) for row in board]))

    #asks for coordinates and prints the contents   
    col_s, row_s = input("Input coordinates (x,y): ").split()
    col = int(col_s)
    row = int(row_s)
    if board[row][col] == " ": 
        print("Empty box, please try again")
        
    #Checks movement of "Pv" pawns
    elif board[row][col] == "Pv":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) == 1:
            board[int(new_positiony)][int(new_positionx)] = "Pv"
            board[row][col] = " "
        else:
            print("Invalid movement")

    #Checks movement of "P^" pawns
    elif board[row][col] == "P^":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) == -1:
            board[int(new_positiony)][int(new_positionx)] = "P^"
            board[row][col] = " "
        else:
            print("Invalid movement")
    
    #Checks movement of "Lv"
    elif board[row][col] == "Lv":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) <= 9:
            board[int(new_positiony)][int(new_positionx)] = "Lv"
            board[row][col] = " "
        else:
            print("Invalid movement")

    #Checks movement of "L^"
    elif board[row][col] == "L^":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 0 and (int(new_positiony)-row) >= -9:
            board[int(new_positiony)][int(new_positionx)] = "L^"
            board[row][col] = " "
        else:
            print("Invalid movement")
    
    #Checks movement of "Nv"
    elif board[row][col] == "Nv":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 and (int(new_positiony)-row) == 2:
            board[int(new_positiony)][int(new_positionx)] = "Nv"
            board[row][col] = " "
        else:
            print("Invalid movement")

    #Checks movement of "N^"
    elif board[row][col] == "N^":
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if (int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1 and (int(new_positiony)-row) == -2:
            board[int(new_positiony)][int(new_positionx)] = "N^"
            board[row][col] = " "
        else:
            print("Invalid movement")

    #Checks movement of "Rv" or "R^"
    elif board[row][col] == "Rv" or board[row][col] == "R^" :
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if ((int(new_positionx)-col) <= 9 and (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) >= -9 and (int(new_positiony)-row) == 0) or ((int(new_positionx)-col) == 0 and (int(new_positiony)-row) <= 9) or ((int(new_positionx)-col) == 0 and (int(new_positiony)-row) >= -9):
            if board[row][col] == "Rv": 
                board[int(new_positiony)][int(new_positionx)] = "Rv"
            else:
                board[int(new_positiony)][int(new_positionx)] = "R^"
            board[row][col] = " "
        else:
            print("Invalid movement")

    #Checks movement of "Bv" or "B^"
    elif board[row][col] == "Bv" or board[row][col] == "B^" :
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        if int(new_positionx) == col or int(new_positiony) == row:
            print ("Invalid movement")
            pass
        elif (int(new_positionx)-col) <= 9 or (int(new_positionx)-col) >= -9 and (int(new_positiony)-row) <= 9 and (int(new_positiony)-row) >= -9:
            if board[row][col] == "Bv": 
                board[int(new_positiony)][int(new_positionx)] = "Bv"
            else:
                board[int(new_positiony)][int(new_positionx)] = "B^"
            board[row][col] = " "
        

    #Checks movement of "Kv" or "K^"
    elif board[row][col] == "Kv" or board[row][col] == "K^" :
        new_positionx, new_positiony = input("Input new coordinates: ").split()
        
        if ((int(new_positionx)-col) == 1 or (int(new_positionx)-col) == -1) and ((int(new_positiony)-row) == 1 or (int(new_positiony)-row) == -1):
            if board[row][col] == "Kv": 
                board[int(new_positiony)][int(new_positionx)] = "Kv"
            else:
                board[int(new_positiony)][int(new_positionx)] = "K^"
            board[row][col] = " "
        else:
            print("Invalid movement")
               
    else:
        print(board[row][col])