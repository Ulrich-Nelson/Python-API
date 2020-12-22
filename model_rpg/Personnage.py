#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor
from random import randint
from utils import TYPE_ETHNIE

""" Class Personnage """

class Personnage():

    # Constructor
    def __init__(self, name, type_personnage, ethnie, sexe):
        self.name = name # Nom
        self.type_personnage = type_personnage # - Guerrier => 1 - Voleur => 2 - Mage => 3
        self.ethnie = ethnie # "Congo": 1, "Mongolie": 2, "France": 3, "USA": 4, "Japon": 5, "Cote_Ivoire": 6, "Argentine": 7, "Haiti": 8, "Angleterre": 9
        self.sexe = sexe # - Homme - Femmme - Trans
        self.attaque = 0
        self.defense = 0
        self.vitesse = 0
        self.chance = 0
        self.mana = 0
        self.vie = 10
        self.exp = 0
        self.init()

    def init(self):
        if self.name == 'Mike':
            self.attaque = 2
            self.defense = 2
            self.vitesse = 2
            self.chance = 2
            self.mana = 2
            self.vie = 2
            self.exp = 2

        """ Stats type personnage """

        if(self.type_personnage == 1): # - Guerrier
            self.attaque += randint(10, 20)
            self.defense += randint(10, 20)
            self.vitesse += randint(1, 10)
            self.chance += randint(5, 15)
            self.mana += randint(1, 10)
            self.vie += randint(5, 15)

            """ Stats type ethnie """
            if( 1 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 3): # "Congo": 1, "Mongolie": 2, "France": 3
                choix = randint(0, 1)
                if choix: # Si true Defense BUFF & Mana NERF
                    self.defense *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.mana /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false Attaque BUFF & Vitesse NERF
                    self.attaque *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.vitesse /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.defense *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.attaque *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.mana /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vitesse /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)






        elif(self.type_personnage == 2): # - Voleur
            self.attaque += randint(5, 15)
            self.defense += randint(1, 10)
            self.vitesse += randint(10, 20)
            self.chance += randint(10, 20)
            self.mana += randint(5, 15)
            self.vie += randint(1, 10)

            """ Stats type ethnie """
            if( 4 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 6): # "USA": 4, "Japon": 5, "Cote_Ivoire": 6
                choix = randint(0, 1)
                if choix: # Si true vitesse BUFF & defense NERF
                    self.vitesse *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.defense /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false chance BUFF & vie NERF
                    self.chance *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.vie /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.vitesse *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.chance *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.defense /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vie /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)


        elif(self.type_personnage == 3):
            self.attaque += randint(1, 10)
            self.defense += randint(5, 15)
            self.vitesse += randint(5, 15)
            self.chance += randint(1, 10)
            self.mana += randint(10, 20)
            self.vie += randint(10, 20)

            """ Stats type ethnie """
            if( 7 >= TYPE_ETHNIE.get(self.ethnie, 3) <= 9): # "Argentine": 7, "Haiti": 8, "Angleterre": 9
                choix = randint(0, 1)
                if choix: # Si true mana BUFF & attaque NERF
                    self.mana *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.attaque /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else: # Si false vie BUFF & chance NERF
                    self.vie *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                    self.chance /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)

            """ Stats sexe """
            if self.sexe == 1:
                choix = randint(0, 1) # BUFF
                if choix:
                    self.mana *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.vie *= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                choix = randint(0, 1) # NERF
                if choix:
                    self.attaque /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
                else:
                    self.chance /= (1+TYPE_ETHNIE.get(self.ethnie, 3)/100)
        
        self.attaque = floor(self.attaque)
        self.defense = floor(self.defense)
        self.vitesse = floor(self.vitesse)
        self.chance = floor(self.chance)
        self.mana = floor(self.mana)
        self.vie = floor(self.vie)


    def __str__(self):
        return "attaque: " + str(self.attaque)+"\n"+ "defense: " + str(self.defense)+"\n"+ "vitesse: " + str(self.vitesse)+"\n"+ "chance: " + str(self.chance)+"\n"+ "mana: " + str(self.mana)+"\n"+ "vie: " + str(self.vie)+"\n"

if __name__ == "__main__":
    test = Personnage('Mike', 1, 'France', 1)
    print(test)