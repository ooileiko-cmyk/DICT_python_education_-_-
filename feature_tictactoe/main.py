board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))


print_board()