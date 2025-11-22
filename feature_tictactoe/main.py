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


    def check_winner():

        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        return None


    winner = check_winner()
    if winner:
        print_board()
        print(f"Игрок {winner} победил! 🎉")
        break

        if all(cell != " " for row in board for cell in row):
            print_board()
            print("Ничья! 🤝")
            break