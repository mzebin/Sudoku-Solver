
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

