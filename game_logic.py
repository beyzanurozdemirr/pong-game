import random

BOARD_SIZE = 8
SHIP_SIZES = [2, 3, 4]

def create_empty_board():
    return [['~' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def place_ships_randomly(board):
    for ship_size in SHIP_SIZES:
        placed = False
        while not placed:
            direction = random.choice(['H', 'V'])
            if direction == 'H':
                row = random.randint(0, BOARD_SIZE - 1)
                col = random.randint(0, BOARD_SIZE - ship_size)
                if all(board[row][col + i] == '~' for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row][col + i] = 'S'
                    placed = True
            else:
                row = random.randint(0, BOARD_SIZE - ship_size)
                col = random.randint(0, BOARD_SIZE - 1)
                if all(board[row + i][col] == '~' for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row + i][col] = 'S'
                    placed = True

def is_game_over(board):
    for row in board:
        if 'S' in row:
            return False
    return True
