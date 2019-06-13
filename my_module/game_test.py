import game

count_row = 6
count_column = 7

def board_starts_empty():
    board = game.game_board()
    for r in range(count_row):
        for c in range(count_column):
            assert board[r][c] == 0:

def check_piece_added():
    board = game.game_board()
    game.add_piece(board, 0, 1)
    assert board[count_row - 1][0] == 1:
    
def run():
    print("Running tests")
    board_starts_empty()
    check_piece_added()
