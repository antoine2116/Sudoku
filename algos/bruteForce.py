import copy
import json

global board
with open("grille_9.json", "r") as file:
    board = json.load(file)

def main():
    printBoard()
    solve()
    printBoard()


def solve():
    global board

    try:
        fillObvious()
    except:
        print("aaaaaaaa")
        return False

    if isComplete():
        return True

    i, j = 0, 0
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                i, j = row, col

    possibilities = getPossibilities(i, j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
        board[i][j] = value
        result = solve()
        if result == True:
            return True
        else:
            board = copy.deepcopy(snapshot)

    return False


def fillObvious():
    global board
    while True:
        change = False
        for i in range(0, 9):
            for j in range(0, 9):
                possibilities = getPossibilities(i, j)
                if not possibilities:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    change = True

        if not change:
            return


def checkValue(row, col, v):
    # Ligne
    for i in range(0, 9):
        if board[row][i] == v and col != i:
            return False

    # Colonne
    for i in range(0, 9):
        if board[i][col] == v and row != i:
            return False
    # Block
    div = 3
    start_row = row // div
    start_col = col // div
    for r in range(start_row * div, (start_row * div) + div):
        for c in range(start_col * div, (start_col * div) + div):
            if board[r][c] == v and row != r and col != c:
                return False
    return True


def getPossibilities(i, j):
    global board
    if board[i][j] != 0:
        return False

    possibilities = []
    for v in range(1, 10):
        if checkValue(i, j, v):
            possibilities.append(v)

    return possibilities

def isComplete():
    for row in board:
        for col in row:
            if (col == 0):
                return False

    return True

def printBoard():
    for row in board:
        print(row)
    print("")

main()