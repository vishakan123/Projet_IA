def initialiser_plateau():
      plateau = []
      for i in range(19):
        ligne = [' ']*19
        plateau.append(ligne)
      return plateau
      
def afficher_plateau(plateau):
     for ligne in plateau:
        ligne_affichee = ""
        for symbole in ligne:
            ligne_affichee += f" {symbole} |"  # Ajouter un espace avant et après chaque symbole, et une barre verticale après
        print(ligne_affichee[:-1])  # Pour enlever le dernier "|"
        print(" " + "- " * (len(ligne)))  # Afficher une ligne de séparation avec un espace avant chaque tiret
 
def joueur_fait_un_coup(plateau, ligne, colonne, symbole) :
    plateau[ligne][colonne]=symbole


def main():
    plateau = initialiser_plateau()
    print("Plateau initial :")
    afficher_plateau(plateau)
    
    print("\nJoueur fait un coup :")
    joueur_fait_un_coup(plateau, 3, 4, 'X')  # Exemple de coup du joueur
    
    print("\nPlateau après le coup :")
    afficher_plateau(plateau)

if __name__ == "__main__":
    main()


