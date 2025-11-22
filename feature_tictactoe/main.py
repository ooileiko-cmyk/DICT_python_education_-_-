board = [[" " for _ in range(3)] for _ in range(3)]
def print_board():
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))


print_board()

player = "X"

while True:
    print_board()
    try:
        row, col = map(int, input(f"Игрок {player}, введите строку и столбец (0-2 через пробел): ").split())
        if row not in range(3) or col not in range(3):
            print("Неверные координаты! Попробуй снова.")
            continue
        if board[row][col] != " ":
            print("Клетка занята! Попробуй снова.")
            continue
        board[row][col] = player
    except ValueError:
        print("Нужно ввести два числа через пробел! Попробуй снова.")
        continue

    player = "O" if player == "X" else "X"