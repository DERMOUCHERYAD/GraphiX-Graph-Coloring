from math import *
import matplotlib.pyplot as plt
import networkx as nx
from pysat.solvers import Glucose3

#_________________________________________________________________________________
def creer_Dimac_fich(graphe, couleurs, nomfich):
    with open(nomfich, 'w') as file:
        voisins=graphe['graphe']
        nb_aretes=graphe['nba']
        nb_sommet = len(voisins)
        nb_couleur = len(couleurs)
        if nb_couleur >1 :
            # en tete premiere ligne ca commence toujour avec un p puis la forme normal conj
            file.write(
                f'p cnf {nb_sommet * nb_couleur} {int(nb_sommet + (nb_sommet*(factorial(nb_couleur)/(factorial(nb_couleur-2)*2))+( nb_aretes* nb_couleur)))}\n')
        else :
            if nb_sommet == 1:
                file.write(
                    f'p cnf {nb_sommet * nb_couleur} {1}\n')
            else :
                print("erreur")

            # num_vertices * num_colors represente le nombre variable car pour chaque variable represente un couple sommet couleur
            # le nombre de clause est calcule comme suit :
            # nb_sommet repersente la contraite que chaque sommet doit avoir une couleur
            # +
            # (factorial(nb_couleur)/(factorial(nb_couleur-2)*2) chaque sommet doit avoir une seule et unique couleur
            # +
            # graphe['nba'])*nb_couleur deux sommet adjacent n'ont pas la meme couleur
            # Contrainte 1: Chaque sommet doit être coloré avec au moins une couleur
        diff=0
        for s in range (nb_sommet):
            clause = ' '.join([f'{diff+color}' for color in couleurs]) + ' 0\n'
            diff+=nb_couleur
            file.write(clause)


            # Contrainte 2: Chaque sommet doit avoir une seule et unique couleur
        for i in range(nb_sommet):
            for j in range(nb_couleur):
                for k in range(j + 1, nb_couleur):
                    file.write(f'-{(i+1) * nb_couleur - j} -{(i+1) * nb_couleur - k} 0\n')

            # Contrainte 3: Deux sommets adjacents ne peuvent pas avoir la même couleur
        for i in range(nb_sommet):
            for voisin in voisins[i]:
                if i < voisin:
                    for k in range(nb_couleur):
                        file.write(f'-{(i+1) * nb_couleur - k} -{(voisin) * nb_couleur - k} 0\n')

#_________________________________________________________________________________
def solve_sat_from_dimacs_file(dimacs_file):
    # Créer une instance du solveur Glucose3
    with Glucose3() as solver:
        # Lire les clauses à partir du fichier DIMACS
        with open(dimacs_file, 'r') as file:
            for line in file:
                if line.startswith('c') or line.startswith('p'):
                    continue
                clause = list(map(int, line.strip().split()[:-1]))
                # Ajouter la clause au solveur
                solver.add_clause(clause)

        # Résoudre le problème SAT
        solution=[]
        if solver.solve():
            solution_exists = True
            print("Solution trouvée:")
            print(solver.get_model())
            solution=solver.get_model()

        else:
            solution_exists = False
            print("Aucune solution trouvée.")
        return solution,solution_exists
#_________________________________________________________________________________
def interprete_solution(solution,nbc):
    colors = {}
    sommet=1
    for i in solution:
        if i > 0:
            if i%nbc == 0 :
                colors[sommet] = (i % nbc) + nbc
                sommet += 1
            else :
                colors[sommet] = (i % nbc)
                sommet += 1
    for sommet, couleur in colors.items():
        print(f"Sommet {sommet} est coloré avec la couleur {couleur}.")
    return colors

#_________________________________________________________________________________
#_________________________________________________________________________________

#_________________________________________________________________________________


# Exemple d'utilisation
graphe = {
   'graphe': [[2,4], [1, 3], [2, 4],[1, 3]],
    'nba': 4 #Number of edges
 }
colors = [1,2,3,4]
creer_Dimac_fich(graphe, colors, 'inst.dimacs')
solution_sat=solve_sat_from_dimacs_file("inst.dimacs")


