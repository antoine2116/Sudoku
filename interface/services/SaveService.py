import json


class SaveService:
    """
    Services managing the save and the loading of the player's games
    """

    def __init__(self):
        """
        Initializes properties
        """

        self.storage_dir = "./storage/"
        self.ext = ".json"

    def getData(self, file_name):
        """
        Read the JSON where the game data is store
        :param file_name: file name
        :return: JSON object containing all the game data
        """

        path = self.storage_dir + file_name + self.ext
        with open(path, "r") as file:
            return json.load(file)

    def saveData(self, file_name, game_widget):
        """
        Saves the game data
        :param file_name: file name
        :param game_widget: widget that contains the grid and the controls panel
        """

        time = game_widget.controls.timer.curr_time
        grid = game_widget.grid
        grid_data = []
        i = 0

        # Go through all the cells of the grid
        for row in range(0, grid.n):
            li = []
            for col in range(0, grid.n):
                cell = grid.cells[i]
                cell_value = cell.cell_value
                cells_hints = cell.cells_hints

                hints = []
                for cell_hint in [c for c in cells_hints if c.value != 0]:
                    hints.append(cell_hint.value)

                player = cell_value.value if (cell_value.fixed and cell_value.checked) or not cell_value.fixed else 0
                solution = cell_value.value if cell_value.fixed and not cell_value.checked else 0
                display_solution = solution != 0
                checked = cell_value.checked

                # Create the JSON object of a cell
                cell_data = {
                    "hints": hints,
                    "player": player,
                    "solution": solution,
                    "display_solution": display_solution,
                    "checked": checked
                }

                li.append(cell_data)
                i = i + 1
            grid_data.append(li)

        # Create the JSON object of the game
        data = {
            "n": grid.n,
            "divider": grid.divider,
            "timer": [time.hour(), time.minute(), time.second()],
            "grid": grid_data
        }

        # Create overwrite or create the save file
        path = self.storage_dir + file_name + self.ext
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

