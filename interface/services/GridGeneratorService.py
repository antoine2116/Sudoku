from math import isqrt
from random import sample


class GridGeneratorService:
    """
    Generates grid and store it into a JSON object
    A portion of the code was found here : https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python (Alain T.)
    """

    def __init__(self, n):
        """
        Initializes propeties
        :param n: size of the grid
        """

        self.n = n
        self.divider = isqrt(n)

    def pattern(self, r, c):
        return (self.divider * (r % self.divider) + r // self.divider + c) % self.n

    def shuffle(self, s):
        return sample(s, len(s))

    def generate(self, difficulty):
        # Generate the grid
        rDivdier = range(self.divider)
        rows = [g * self.divider + r for g in self.shuffle(rDivdier) for r in self.shuffle(rDivdier)]
        cols = [g * self.divider + c for g in self.shuffle(rDivdier) for c in self.shuffle(rDivdier)]
        nums = self.shuffle(range(1, self.divider * self.divider + 1))

        self.grid = [[nums[self.pattern(r, c)] for c in cols] for r in rows]

        # Removing some cell according to the difficulty
        diff = 3 if difficulty == "Difficile" else 2
        blocks = self.n * self.n
        empties = blocks * diff // 4
        for p in sample(range(blocks), empties):
            self.grid[p // self.n][p % self.n] = 0

        # Converts matrix into a JSON object
        grid_data = []
        for r in range(0, self.n):
            line = []
            for c in range(0, self.n):
                cell = {
                    "hints": [],
                    "player": 0,
                    "solution": self.grid[r][c],
                    "display_solution": self.grid[r][c] != 0,
                    "checked": False
                }
                line.append(cell)
            grid_data.append(line)

        soduku_data = {
            "n": self.n,
            "divider": self.divider,
            "timer": [0, 0, 0],
            "grid": grid_data
        }

        return soduku_data
