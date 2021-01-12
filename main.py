from grille import *

grille = Grille(16)
grille.afficher()
"""
# Test reussite
if grille.proposer(6, 1, 4):
    print("Bravo ! \n")
else:
    print("Echec... \n")

grille.afficher()

# Test Echec
if grille.proposer(9, 2, 1):
    print("Bravo ! \n")
else:
    print("Echec... \n")

grille.afficher()
grille.sauvegarder()
"""