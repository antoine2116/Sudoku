import json


class SauvegardeService:
    storage_dir = "./storage/"
    ext = ".json"

    def __init__(self):
        pass

    def getData(self, file_name):
        path = self.storage_dir + file_name + self.ext
        print(path)
        with open(path, "r") as file:
            return json.load(file)

    def saveData(self, file_name, jeu_widget):
        time = jeu_widget.controls.timer.curr_time
        grille = jeu_widget.grille
        grille_data = []
        cpt = 0
        for i in range(0, grille.n):
            li = []
            for y in range(0, grille.n):
                cellule = grille.cells[cpt]
                cell_valeur = cellule.cell_valeur
                cells_indices = cellule.cells_indices

                indices = []
                for cell_indice in [c for c in cells_indices if c.value != 0]:
                    indices.append(cell_indice.value)

                joueur = cell_valeur.value if not cellule.fixed else 0
                solution = cell_valeur.value if cellule.fixed else 0
                afficher_solution = solution != 0
                verifie = cell_valeur.verifie

                cell_data = {
                    "indices": indices,
                    "joueur": joueur,
                    "solution": solution,
                    "afficher_solution": afficher_solution,
                    "verifie": verifie
                }

                li.append(cell_data)
                cpt = cpt + 1
            grille_data.append(li)


        data = {
            "n": grille.n,
            "divider": grille.divider,
            "timer": [time.hour(), time.minute(), time.second()],
            "grille": grille_data
        }

        path = self.storage_dir + file_name + self.ext

        with open(path, "w") as file:
            json.dump(data, file, indent=4)

