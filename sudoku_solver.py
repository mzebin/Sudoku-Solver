
def in_col(board, row, col, digit):
    for y  in range(len(board)):
        if board[y][col] == digit:
            return True

    return False


def in_row(board, row, col, digit):
    for x in range(len(board)):
        if board[row][x] == digit:
            return True

    return False


def in_box(board, start_row, start_col,   digit):
    for row in range(3):
        for col in range(3):
            if board[row + start_row][col + start_col] == digit:
                return True

    return False


def is_valid_spot(board, row, col, digit):
    return not in_row(board, row, col, digit) and \
            not in_col(board, row, col, digit) and \
            not in_box(board, row - row % 3, col - col % 3, digit)


def get_empty_spot(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "_":
                return row, col

    return -1, -1


def solve_sudoku(board):
    row, col = get_empty_spot(board)
    
    if row == col == -1:
        return True

    for digit in range(1, 10):
        digit = str(digit)
        if is_valid_spot(board, row, col, digit):
            board[row][col] = digit

            if solve_sudoku(board):
                return True

            board[row][col] = "_"

    return False


def print_board(board):
    for idx1, row in enumerate(board):
        if idx1 % 3 == 0:
            print("-" * 43)
        for idx2, value in enumerate(row):
            if idx2 % 3 == 0:
                print("| ", end="")
            print(" " + value, end="  ")
        print("|")
    print("-" * 43)


board = [
    ["_", "3", "_", "_", "_", "_", "_", "8", "_"],
    ["5", "_", "_", "_", "6", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "8", "2", "1", "9"],
    ["_", "_", "7", "9", "_", "_", "_", "6", "_"],
    ["_", "_", "_", "_", "_", "7", "_", "_", "2"],
    ["_", "_", "_", "2", "_", "_", "1", "_", "_"],
    ["_", "7", "1", "3", "4", "_", "_", "_", "_"],
    ["2", "_", "_", "_", "_", "_", "4", "_", "3"],
    ["_", "_", "9", "_", "_", "_", "_", "_", "_"],
]

print_board(board)
print()
print("-" * 50)
solve_sudoku(board)
print("-" * 50)
print()
print_board(board)

