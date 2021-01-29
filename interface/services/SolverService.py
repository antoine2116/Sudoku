import copy


class SolverService:
    """
    Service offering tools to solve of check a sudoku grid
    """
    def __init__(self, grid):
        """
        Initialize properties
        :param grid: Grid object
        """

        self.grid = grid
        self.n = grid.n
        self.divider = grid.divider
        self.grid_data = []

    def loadGridData(self):
        """
        Extracts the grid from to object in order to work with a matrix
        """

        i = 0
        for r in range(0, self.n):
            li = []
            for c in range(0, self.n):
                li.append(self.grid.cells[i].cell_value.value)
                i = i + 1
            self.grid_data.append(li)

    def checkValue(self, row, col, v):
        """
        Checks wheter a value is valid or not in a specific cell
        :param row: (int) row number
        :param col: (int) column number
        :param v: (int) value to test
        :return: (bool) whether the value is valid or not
        """

        # Row
        for i in range(self.n):
            if self.grid_data[row][i] == v and col != i:
                return False

        # Column
        for i in range(self.n):
            if self.grid_data[i][col] == v and row != i:
                return False

        # Box
        div = self.divider
        start_row = row // div
        start_col = col // div
        for r in range(start_row * div, (start_row * div) + div):
            for c in range(start_col * div, (start_col * div) + div):
                if self.grid_data[r][c] == v and row != r and col != c:
                    return False
        return True

    def checkGrid(self):
        """
        Checks if the player's grid is valid or not
        :return: (int)(int) number of correct guess and incorrect guesses
        """

        self.loadGridData()

        success = 0
        fails = 0
        i = 0

        # Test each cell
        for r in range(0, self.grid.n):
            for c in range(0, self.grid.n):
                cell = next((cell.cell_value for cell in self.grid.cells if cell.r == r and cell.c == c), None)
                if not cell.fixed and cell.value != 0:
                    if self.checkValue(r, c, cell.value):
                        self.checkCell(r, c, cell.value)
                        success = success + 1
                    else:
                        fails = fails + 1
                i = i + 1

        return success, fails

    def getPossibilities(self, row, col):
        """
        Get the list of values that are possible to put in a specific cell
        :param row: row number
        :param col: col numer
        :return: list of possibles values
        """

        if self.grid_data[row][col] != 0:
            return False

        possibilities = []
        for i in range(1, self.n + 1):
            if self.checkValue(row, col, i):
                possibilities.append(i)

        return possibilities

    def autoComplete(self, selected_cell):
        """
        Fills the cell which have only one possibility and which are on the same row, column and box as the selected cell
        Called when a player change the value of a cell
        :param selected_cell: selected cell
        """

        self.loadGridData()
        cells_to_check = []

        # Find the empty cells in the same row
        row_cells = [cell for cell in self.grid.cells if
                        not cell.cell_value.fixed and cell.r == selected_cell.r and cell.cell_value.value == 0]
        if len(row_cells) == 1:
            cells_to_check.append(row_cells[0])

        # Find the empty cells in the same column
        col_cells = [cell for cell in self.grid.cells if
                          not cell.cell_value.fixed and cell.c == selected_cell.c and cell.cell_value.value == 0]
        if len(col_cells) == 1:
            cells_to_check.append(col_cells[0])

        # Find the empty cells in the same box
        box_cells = []
        div = self.divider
        start_row = selected_cell.r // div
        start_col = selected_cell.c // div
        for r in range(start_row * div, (start_row * div) + div):
            for c in range(start_col * div, (start_col * div) + div):
                cell = next((cell for cell in self.grid.cells if
                             not cell.cell_value.fixed and cell.r == r and cell.c == c and cell.cell_value.value == 0), None)
                if cell is not None and cell not in cells_to_check:
                    box_cells.append(cell)
        if len(box_cells) == 1:
            cells_to_check.append(box_cells[0])

        # Check each cells, if there is only one possibility, it fill it
        for cell in cells_to_check:
            possibilities = self.getPossibilities(cell.r, cell.c)
            if possibilities and len(possibilities) == 1:
                cell.updateValue(int(possibilities[0]))

    def gridResolved(self):
        """
        Checks whether the grid if resolved or not
        :return: (bool) whether the grid if resolved or not
        """

        for row in self.grid_data:
            for col in row:
                if col == 0:
                    return False

        return True

    def solveByBruteForce(self):
        """
        Entry point of the brute force algorithm
        """

        tries = 0
        while tries < 10:
            self.fillObvious()
            tries += 1

    def solveByBackTracking(self):
        """
        Entry point of the back track algorithm
        """

        # First, we try all the obvious possibilities
        try:
            self.fillObvious()
        except Exception as e:
            return False

        # If the grid is resolved, we can stop
        if self.gridResolved():
            return True

        # Find the next empty cell
        r, c = 0, 0
        for row in range(0, self.n):
            for col in range(0, self.n):
                if self.grid_data[row][col] == 0:
                    r, c = row, col

        # Try to set its value with one of the possibilities
        possibilities = self.getPossibilities(r, c)
        if possibilities:
            for value in possibilities:
                # Make a copy of the grid it was not a good solution
                snapshot = copy.deepcopy(self.grid_data)
                self.checkCell(r, c, value)
                result = self.solveByBackTracking()
                # If the grid is resolved, we can stop here
                if result:
                    return True
                # However, if the grid is not resolved, we go back to the last copy
                else:
                    self.grid_data = copy.deepcopy(snapshot)

        return False

    def fillObvious(self):
        """
        Fills all cells that have only one possibility
        :return: whether a change occurs or not
        """

        while True:
            change = False
            for r in range(0, self.n):
                for c in range(0, self.n):
                    possibilities = self.getPossibilities(r, c)
                    if not possibilities:
                        continue
                    if len(possibilities) == 1:
                        self.checkCell(r, c, possibilities[0])
                        change = True

            if not change:
                return

    def checkCell(self, row, col, value):
        """
        Fills a cell with a value and checked it
        :param row: row number
        :param col: col number
        :param value: incoming value
        """

        self.grid_data[row][col] = value

        cell = next((cell.cell_value for cell in self.grid.cells if cell.r == row and cell.c == col), None)
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        cell.setText(symbols[value])

        cell.value = value
        cell.fixed = value != 0
        cell.checked = value != 0
        cell.updateStyle()