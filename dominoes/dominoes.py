import random
from collections import Counter


def create_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def distribute(dominoes):
    while True:
        random.shuffle(dominoes)

        stock = dominoes[:14]
        computer = dominoes[14:21]
        player = dominoes[21:]

        max_double = None
        max_value = -1

        for p in stock + computer + player:
            if p[0] == p[1] and p[0] > max_value:
                max_double = p
                max_value = p[0]

        if max_double:
            if max_double in computer:
                status = "computer"
                computer.remove(max_double)
            else:
                status = "player"
                player.remove(max_double)

            snake = [max_double]
            return stock, computer, player, snake, status

        def print_state(stock, computer, player, snake, status):
            print("=" * 70)
            print(f"Stock size: {len(stock)}")
            print(f"Computer pieces: {len(computer)}")

            if len(snake) <= 6:
                print(*snake, sep="")
            else:
                print(*snake[:3], sep="", end="")
                print("...", end="")
                print(*snake[-3:], sep="")

            print("Your pieces:")
            for i, p in enumerate(player):
                print(f"{i + 1}:{p}")

            if status == "player":
                print("Status: It's your turn to make a move. Enter your command.")
            else:
                print("Status: Computer is about to make a move. Press Enter to continue...")

                def can_place(piece, snake, side):
                    left = snake[0][0]
                    right = snake[-1][1]

                    if side == "left":
                        return piece[1] == left or piece[0] == left
                    else:
                        return piece[0] == right or piece[1] == right

                def place_piece(piece, snake, side):
                    left = snake[0][0]
                    right = snake[-1][1]

                    if side == "left":
                        if piece[0] == left:
                            snake.insert(0, piece)
                        else:
                            snake.insert(0, piece[::-1])
                    else:
                        if piece[1] == right:
                            snake.append(piece)
                        else:
                            snake.append(piece[::-1])