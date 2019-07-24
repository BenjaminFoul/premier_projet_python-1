# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:02:50 2019

@author: Guillaume
"""

'''Nombre à deviner'''
from random import randint

entier = randint(1,1000)

print("Bienvenue dans l'emission intitulée : LE JUSTE PRIX")

for nb_essais in range(1,11):
    print("Il vous reste",11-nb_essais,"essai(s).")
    '''Proposition de l'utilisateur'''
    entree = int(input("Entrez un prix :\n"))
    '''Test sur les essais'''
    if nb_essais != 10:
        if entree < entier:
            print("C'est plus !")
        elif entree > entier:
            print("C'est moins !")
        else:
            break

'''On vérifie ici la condition de victoire'''
if entree != entier :
    print("C'est perdu ! Le juste prix était :",entier,"!")
else:
    print("C'est gagné !")

print("Merci d'avoir participé ! A bientôt dans le juste prix !")
