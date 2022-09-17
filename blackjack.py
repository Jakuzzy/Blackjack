import random as rd

#Constantes
liste_faces = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
liste_signes = ['♥','♦','♣','♠']

#Fonctions
"""
carte = une liste sous la forme [('face','signe'),'valeur']
main = une liste de cartes sous la forme ['carte','carte',...]
"""

def tirage(nb=2):
    main = []
    for _ in range(nb):
        face = rd.choice(liste_faces)
        if face == '1':
            valeur = 11
        elif face in '2,3,4,5,6,7,8,9':
            valeur = int(face)
        else:
            valeur = 10
        main.append([(face,rd.choice(liste_signes)),valeur])
    return main

def total(main):
    total = 0
    for carte in main:
        total += carte[1]
    if total > 21:
        for carte in main:
            if carte[0][0]=='1' and total > 21:
                carte[1] = 1
                total -= 10
            elif total <= 21:
                break
    return total
