import json
import os.path
import math
import time


class Grille:
    # Constructeur
    def __init__(self, n):
        self.n = n
        self.tabL = []
        self.tabC = []
        self.index = -1

        path_joueur = 'grilles/joueurs/grille_' + str(n) + '0.json'
        path_indices = 'grilles/joueurs/grilleIndices' + str(n) + '.json'
        path_solution = 'grilles/solutions/grille_' + str(n) + '.json'

        # Si on a un fichier joueur, on l'ouvre
        if os.path.isfile(path_joueur):
            fichier = open(path_joueur, 'r')

        # Sinon, on ouvre le fichier solution (fichier vide)
        elif os.path.isfile(path_solution):
            fichier = open(path_solution, 'r')

        # On prépare les indices
        fichierIncides = open(path_indices, 'r')

        self.m = json.load(fichier)
        self.mIndi = json.load(fichierIncides)
        fichier.close()

    # Permet d'afficher la grille
    def afficher(self):
        if self.n == 9:
            for l in range(self.n):
                ligne = ""
                if l == 3 or l == 6:  # 3 et 6 temporaire (fonctionne uniquement sur des grille 9x9)
                    print("---------------------")
                for c in range(self.n):
                    if c == 3 or c == 6:  # 3 et 6 temporaire (fonctionne uniquement sur des grille 9x9)
                        ligne += "| "
                    if self.m[l][c] > 0:
                        # if self.m[l][c] > 9:
                        # ligne += self.convertisseur(self.m[l][c]) + " "
                        # else:
                        ligne += str(self.m[l][c]) + " "
                    else:
                        ligne += "0 "
                print(ligne)

        # if self.n == 16:
        # for l in range(self.n):
        # ligne = ""
        # if l == 4 or l == 8 or l == 12:
        # print("-------------------------------------")
        # for c in range(self.n):
        # if c == 4 or c == 8 or c == 12:
        # ligne += "| "
        # if self.m[l][c] > 0:
        # if self.m[l][c] > 9:
        # ligne += self.convertisseur(self.m[l][c]) + " "
        # else:
        # ligne += str(self.m[l][c]) + " "
        # else:
        # ligne += "0 "
        # print(ligne)

    # Permet de passer les nombres en lettre
    def convertisseur(self, chiffre):
        lettres = ["", "", "", "", "", "", "", "", "", "A", "B", "C", "D", "E", "F", "G"]
        return lettres[chiffre - 1]

    # Permet de savoir si la grille est resolue
    def resolue(self):
        for l in range(self.n):
            for c in range(self.n):
                if (self.m[l][c] < 0):
                    return False

    # Permet d'afficher le chiffre trouve
    def decouvrir(self, p, l, c):
        self.m[l][c] = p

    # Permet de proposer un nombre
    def proposer(self, p, l, c):
        approved = True
        # On ajuste les index (saisie plus amicale)
        l = l - 1
        c = c - 1

        # Ligne
        for col in range(self.n):
            if self.m[l][col] == p:
                approved = False

        # Colonne
        for lig in range(self.n):
            if self.m[lig][c] == p:
                approved = False

        # Block
        diviseur = int(self.n / 3)
        c_block = int(math.floor(c / diviseur) * diviseur)
        l_block = int(math.floor(l / diviseur) * diviseur)

        for i in range(self.n // 3):
            for y in range(self.n // 3):
                if self.m[l_block + i][c_block + y] == p:
                    approved = False

        if approved:
            self.decouvrir(p, l, c)

        return approved

    def sauvegarder(self):
        path_joueur = 'grilles/joueurs/grille_' + str(self.n) + '.json'
        # Si on a un fichier joueur, on l'ouvre
        if os.path.isfile(path_joueur):
            fichier = open(path_joueur, 'w');
        # Sinon, on en cree un
        else:
            fichier = open(path_joueur, 'a')

        # On remplace / ajoute la nouvelle grille
        json.dump(self.m, fichier, indent=4, sort_keys=True)
        fichier.close()

    def ajouterIndice(self, p, l, c):
        self.mIndi[l][c].append(p)

    def affichageIndice(self, l, c):
        for i in range(len(self.mIndi[l][c])):
            print(self.mIndi[l][c][i])

    def VerifPossibilite(self, l, c):
        n = self.n
        tab = []

        for i in range(n):
            i = i + 1
            if self.proposer(i, l, c):
                tab.append(i)

        for y in range(len(tab)):
            print(tab[y])

    def caseEmpty(self, l, c):
        if self.m[l][c] <= 0:
            return 0
        else:
            return 1

    def retour(self, l, c):
        return self.m[l][c]

    def forceBack(self, p, l, c):  # regarder le probleme
        print(p)
        check = 0
        i = 1
        y = 2

        while check == 0:
            self.forceZero(l, c)
            print("p = " + str(p) + "i = " + str(i))
            if p + i > 9:
                print("supérieur à 9")
                self.back(-y)
                print("-y " + str(-y))
                y = y + 1
                i = 1
            if self.proposer(p + i, l + 1, c + 1) == True:
                print("force l " + str(l + 1) + " force c " + str(c + 1) + "  t=" + str(p + i))
                self.afficher()
                del self.tabL[y + 1:]
                check = 1
            else:
                i = i + 1

    def stockTentatives(self, l, c):
        self.tabL.append(l)
        self.tabC.append(c)

    def back(self, index):

        l = self.tabL[index]
        c = self.tabC[index]
        t = self.retour(l, c)
        # print(index)
        print("ancien l " + str(l) + " ancien c " + str(c) + " t " + str(t))

        self.forceBack(t, l, c)

    def forceZero(self, l, c):
        self.m[l][c] = 0

    ##### brute force #####
    # Test la grille ligne par ligne

    def testValeur(self, grid: list, i: int, j: int) -> list:

        ligne_remplie = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for IndexLigne in range(9):
            ligne_remplie[grid[i][IndexLigne]] = 1
        for IndexColonne in range(9):
            ligne_remplie[grid[IndexColonne][j]] = 1
        # Pour un carré de 3 X 3
        col_start, row_start = i // 3 * 3, j // 3 * 3
        for IndexLigne in range(row_start, row_start + 3):
            for IndexColonne in range(col_start, col_start + 3):
                ligne_remplie[grid[IndexColonne][IndexLigne]] = 1
        return ligne_remplie

    def AlgoBruteForce(self):
        count = 1
        while count != 0:
            count2 = 0
            for i in range(9):
                for j in range(9):
                    if self.m[i][j] == 0:
                        intList = self.testValeur(self.m, i, j)
                        if sum(intList[1:]) == 8:
                            print("aaa")
                            self.m[i][j] = intList[1:].index(0) + 1
            count = count2

    def lancerBruteForce(self):
        self.AlgoBruteForce()
