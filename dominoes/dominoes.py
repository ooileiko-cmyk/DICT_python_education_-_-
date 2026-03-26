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