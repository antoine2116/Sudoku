from math import isqrt
from random import sample

# Une partie du programme provient d'un post StackOverflow (https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python)
class GenerateurGrille:
    def __init__(self, n):
        self.n = n
        self.divider = isqrt(n)

    def pattern(self, r, c):
        return (self.divider * (r % self.divider) + r // self.divider + c) % self.n

    def shuffle(self, s):
        return sample(s, len(s))

    def generate(self):
        # On génère la grille complète
        rDivdier = range(self.divider)
        rows = [g * self.divider + r for g in self.shuffle(rDivdier) for r in self.shuffle(rDivdier)]
        cols = [g * self.divider + c for g in self.shuffle(rDivdier) for c in self.shuffle(rDivdier)]
        nums = self.shuffle(range(1, self.divider * self.divider + 1))

        self.grille = [[nums[self.pattern(r, c)] for c in cols] for r in rows]

        # On enlève certaines cellules
        blocks = self.n * self.n
        empties = blocks * 3 // 4
        for p in sample(range(blocks), empties):
            self.grille[p // self.n][p % self.n] = 0

        # On convertit la matrix en json
        grille_data = []
        for x in range(0, self.n):
            line = []
            for y in range(0, self.n):
                cell = {
                    "indices": [],
                    "joueur": 0,
                    "solution": abs(self.grille[x][y]),
                    "afficher_solution": self.grille[x][y] != 0,
                    "verifie": False
                }
                line.append(cell)
            grille_data.append(line)

        # On crée le fichier
        soduku_data = {
            "n": self.n,
            "divider": self.divider,
            "grille": grille_data
        }

        return soduku_data