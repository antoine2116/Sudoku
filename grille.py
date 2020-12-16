import json
import os.path
import math

class Grille:
    # Constructeur
    def __init__(self, n):
        self.n = n

        path_joueur = 'grilles/joueurs/grille_' + str(n) + '.json'
        path_indices = 'grilles/joueurs/grilleIndices' + str(n) + '.json'
        path_solution = 'grilles/solutions/grille_' + str(n) + '.json'

        # Si on a un fichier jouer, on l'ouvre
        if os.path.isfile(path_joueur):
            fichier = open(path_joueur, 'r')
            fichierIncides = open(path_indices, 'r')

        # Sinon, on ouvre le fichier solution (fichier vide)
        elif os.path.isfile(path_solution):
            fichier = open(path_solution, 'r')

        self.m = json.load(fichier)
        self.mIndi = json.load(fichierIncides)
        fichier.close()

    #Permet d'afficher la grille
    def afficher(self):
        if self.n == 9:
            for l in range(self.n):
                ligne = ""
                if l == 3 or l == 6: # 3 et 6 temporaire (fonctionne uniquement sur des grille 9x9)
                    print("---------------------")
                for c in range(self.n):
                    if c == 3 or c == 6:  # 3 et 6 temporaire (fonctionne uniquement sur des grille 9x9)
                        ligne += "| "
                    if self.m[l][c] > 0:
                        if self.m[l][c] > 9:
                            ligne += self.convertisseur(self.m[l][c]) + " "
                        else:
                            ligne += str(self.m[l][c]) + " "
                    else:
                        ligne += "0 "
                print(ligne)

    #Permet de passer les nombres en lettre
    def convertisseur(self, chiffre):
        lettres = ["","","","","","","","","","A","B","C","D","E","F"]
        return lettres[chiffre-1]

    # Permet de savoir si la grille est resolue
    def resolue(self):
        for l in range(self.n):
            for c in range(self.n):
                if (self.m[l][c] < 0):
                    return False

    # Permet d'afficher le chiffre trouve
    def decouvrir(self, l, c):
        self.m[l][c] = -self.m[l][c]

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
        diviseur = int(self.n/3)
        c_block = int(math.floor(c/diviseur) * diviseur)
        l_block = int(math.floor(l/diviseur) * diviseur)

        for i in range(self.n//3):
            for y in range(self.n//3):
                if self.m[l_block + i][c_block + y] == p:
                    approved = False
        
        if approved:
            self.decouvrir(l, c)

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

    def ajouterIndice(self,p,l,c):
        self.mIndi[l][c].append(p)

    def affichageIndice(self,l,c):
        for i in range(len(self.mIndi[l][c])):
            print(self.mIndi[l][c][i])

    