import copy


class SolveurService:
    def __init__(self, grille):
        self.grille = grille
        self.n = grille.n
        self.divider = grille.divider
        self.grille_data = []

    def loadGrilleData(self):
        cpt = 0
        for r in range(0, self.grille.n):
            li = []
            for c in range(0, self.grille.n):
                li.append(self.grille.cells[cpt].cell_valeur.value)
                cpt = cpt + 1
            self.grille_data.append(li)

    # Permet de proposer un nombre
    def checkValue(self, row, col, v):
        # Ligne
        for i in range(self.n):
            if self.grille_data[row][i] == v and col != i:
                return False

        # Colonne
        for i in range(self.n):
            if self.grille_data[i][col] == v and row != i:
                return False

        # Block
        div = self.divider
        start_row = row // div
        start_col = col // div
        for r in range(start_row * div, (start_row * div) + div):
            for c in range(start_col * div, (start_col * div) + div):
                if self.grille_data[r][c] == v and row != r and col != c:
                    return False
        return True

    def checkGrille(self):
        self.loadGrilleData()
        success = 0
        fails = 0
        cpt = 0
        for r in range(0, self.grille.n):
            for c in range(0, self.grille.n):
                cell = next((cell.cell_valeur for cell in self.grille.cells if cell.r == r and cell.c == c), None)
                if not cell.fixed and cell.value != 0:
                    if self.checkValue(r, c, cell.value):
                        self.setCellVerifie(r, c, cell.value)
                        success = success + 1
                    else:
                        fails = fails + 1
                cpt = cpt + 1
        return success, fails

    def getPossibilites(self, row, col):
        if self.grille_data[row][col] != 0:
            return False

        possibilites = []
        for i in range(1, self.n + 1):
            if self.checkValue(row, col, i):
                possibilites.append(i)
        return possibilites

    def autoComplete(self, selected_cell):
        self.loadGrilleData()
        cells_to_check = []

        # Ligne
        cells_lignes = [cell for cell in self.grille.cells if
                        not cell.fixed and cell.r == selected_cell.r and cell.cell_valeur.value == 0]
        if len(cells_lignes) == 1:
            cells_to_check.append(cells_lignes[0])

        # Colonne
        cells_colonnes = [cell for cell in self.grille.cells if
                          not cell.fixed and cell.c == selected_cell.c and cell.cell_valeur.value == 0]
        if len(cells_colonnes) == 1:
            cells_to_check.append(cells_colonnes[0])

        # Block
        cells_block = []
        div = self.divider
        start_row = selected_cell.r // div
        start_col = selected_cell.c // div
        for r in range(start_row * div, (start_row * div) + div):
            for c in range(start_col * div, (start_col * div) + div):
                cell = next((cell for cell in self.grille.cells if
                             not cell.fixed and cell.r == r and cell.c == c and cell.cell_valeur.value == 0), None)
                if cell is not None and cell not in cells_to_check:
                    cells_block.append(cell)
        if len(cells_block) == 1:
            cells_to_check.append(cells_block[0])

        for cell in cells_to_check:
            possibilites = self.getPossibilites(cell.r, cell.c)
            if possibilites and len(possibilites) == 1:
                cell.updateValue(int(possibilites[0]))

    def grilleResolved(self):
        for row in self.grille_data:
            for col in row:
                if col == 0:
                    return False
        return True

    def solveByBruteForce(self):
        tries = 0
        while tries < 10:
            self.fillObvious()
            tries += 1

    def solveByBackTracking(self):
        try:
            self.fillObvious()
        except Exception as e:
            return False
        if self.grilleResolved():
            return True

        r, c = 0, 0
        for row in range(0, self.n):
            for col in range(0, self.n):
                if self.grille_data[row][col] == 0:
                    r, c = row, col

        possibilities = self.getPossibilites(r, c)
        for value in possibilities:
            snapshot = copy.deepcopy(self.grille_data)
            self.setCellVerifie(r, c, value)
            result = self.solveByBackTracking()
            if result:
                return True
            else:
                self.grille_data = copy.deepcopy(snapshot)

        return False

    def fillObvious(self):
        while True:
            change = False
            for r in range(0, self.n):
                for c in range(0, self.n):
                    possibilities = self.getPossibilites(r, c)
                    if not possibilities:
                        continue
                    if len(possibilities) == 1:
                        self.setCellVerifie(r, c, possibilities[0])
                        change = True

            if not change:
                return

    def setCellVerifie(self, row, col, value):
        self.grille_data[row][col] = value
        cell = next((cell.cell_valeur for cell in self.grille.cells if cell.r == row and cell.c == col), None)
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        cell.setText(symbols[value])
        cell.value = value
        cell.fixed = value != 0
        cell.verifie = value != 0
        cell.updateTextColor()