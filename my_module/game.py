from IPython.display import clear_output
import numpy as np

count_row = 6
count_column = 7

# Create matrix shape
def print_board(board):
    print("===================")
    print("*  Current Board  *")
    print("===================")
    for r in range(count_row):
        for c in range(count_column):
            print(int(board[r][c]), end="  ")
        print()
    print()
    
# Create matrix of zeros
def game_board():
    return np.zeros(shape=(count_row, count_column))   

# Add pieces within range
def add_piece(board, column, piece):
    piece_placed = False
    for r in range(count_row):
        if board[r][column] != 0:
            board[r - 1][column] = piece
            piece_placed = True
            break
    if not piece_placed:
        board[count_row - 1][column] = piece
        
# Ensure pieces are placed validly 
def valid_piece_placement(board, column):
    filled_spots = 0
    for r in range(count_row):
        if board[r][column] != 0:
            filled_spots += 1
    if filled_spots < count_row:
        return True
    else:
        return False

# Flip board so pieces fall to bottom
def change_board(board):
    print(np.flip(board, 0))

def once_you_win(board, piece):
    # Check row locations for wins
    for c in range(count_column - 3):
        for r in range(count_row):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece \
            and board[r][c + 3] == piece:
                return True
                
    # Check column locations for wins
    for c in range(count_column):
        for r in range(count_row - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r + 2][c] == piece \
            and board[r + 3][c] == piece:
                return True
                
    # Check + slope diagonals
    for c in range(count_column - 3):
        for r in range(count_row - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and\
            board[r + 3][c + 3] == piece:
                return True
                
    # Check - slope diagonals
    for c in range(count_column - 3):
        for r in range(3, count_row):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and\
            board[r - 3][c + 3] == piece:
                return True

            
def play():
    board = game_board()
    end_game = False
    current_player = 1

    while not end_game:
        # Print board
        print_board(board)

        # Make move
        valid_move = False
        while not valid_move:
            # Ask for input
            prompt = "Your turn player " + str(current_player) + "! (0-6): "
            column = int(input(prompt))

            if valid_piece_placement(board, column):
                add_piece(board, column, current_player)
                valid_move = True
            else:
                print("Invalid move! Please pick another column.")

        if once_you_win(board, current_player):
            clear_output()
            print_board(board)
            msg = "Player " + str(current_player) + " wins, YAYYY!!!"
            print(msg)
            end_game = True


        # Change player
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        if not end_game:
            clear_output()
   
