
from utils import Windows
from model_rpg import Personnage, Item


test = Windows()
test.register_personnage()

# name = input('Entrez votre nom:') # Recupération de data sur le terminal
# while True: # Boucle infini
#     type_personnage = input('Entrez votre type (- Guerrier => 1 - Voleur => 2 - Mage => 3):')
#     if type_personnage.isnumeric() : # Check si c'est une valeur numérique
#         if 1 <= int(type_personnage) <= 3: # Check si c'est compris entre 1 et 3 compris
#             type_personnage = int(type_personnage)
#             break # Fin de la boucle
#         else:
#             print("Nb non compris entre 1 et 3")
#     else:
#         print("Valeur non numérique")

# while True: # Boucle infini
#     ethnie = input('Entrez votre ethnie ("Congo", "Mongolie", "France", "USA", "Japon", "Cote_Ivoire", "Argentine", "Haiti", "Angleterre"):')
#     ethnie = ethnie.strip()
#     ethnie = ethnie.capitalize()
#     if ethnie in TYPE_ETHNIE: # Check si la string est dans le dict
#         break
#     else:
#         print("Valeur non reconnu")

# while True: # Boucle infini
#     sexe = input('Entrez votre sexe (- Homme => 1 - Femmme => 2 - Trans => 3):')
#     if sexe.isnumeric() : # Check si c'est une valeur numérique
#         if 1 <= int(sexe) and int(sexe) <= 3: # Check si c'est compris entre 1 et 3 compris
#             sexe = int(sexe)
#             break # Fin de la boucle
#         else:
#             print("Nb non compris entre 1 et 3")
#     else:
#         print("Valeur non numérique")