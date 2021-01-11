import json

m = \
    [
        [4, 3, -9, -6, -1, -2, -5, -7, 8],
        [-6, 7, -1, -5, -8, 3, -4, -2, 9],
        [2, -5, -8, 4, 9, -7, -6, -1, -3],
        [-8, 2, -5, 7, 4, 1, -3, -9, 6],
        [-7, -6, -4, -2, -3, -9, -1, -8, -5],
        [1, -9, -3, 8, 6, 5, -7, 4, -2],
        [-3, -1, -6, -9, 2, 4, -8, -5, 7],
        [5, -8, -2, 1, -7, -6, -9, 3, -4],
        [9, -4, -7, -3, -5, -8, -2, 6, 1]
    ]

grille = []

for x in range(0, 9):
    line = []
    for y in range(0, 9):
        cell = {
            "indices": [],
            "joueur": 0,
            "solution": abs(m[x][y]),
            "afficher_solution": m[x][y] > 0,
        }
        line.append(cell)
    grille.append(line)

json_dump = json.dumps(grille, indent=4)

print(json_dump)

