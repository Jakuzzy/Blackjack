import random as rd

liste_faces = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
liste_signes = ['♥','♦','♣','♠']

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

def blackjack():
    jouer = input("Voulez-vous jouer au Blackjack ? [Y/N] ")
    if jouer.lower() == 'y':
        main_joueur,main_croupier = tirage(),tirage()
        total_joueur,total_croupier, = total(main_joueur),total(main_croupier)
        print("Le jeu du croupier :",[main_croupier[0],'Carte cachée'],"\nVotre jeu :",main_joueur,total_joueur)
        if total_joueur == 21:
            print("Vous gagnez en obtenant un Blackjack !")
        else:
            suite = input("Que voulez-vous faire ? [O]btenir des cartes/[G]arder ses cartes ")
            if suite.lower() == 'o':
                nb_cartes = int(input("Combien de cartes voulez-vous ? [nb] "))
                main_joueur += tirage(nb_cartes)
                total_joueur = total(main_joueur)
            while total_croupier < 17:
                main_croupier += tirage(1)
                total_croupier = total(main_croupier)
            print("Le jeu du croupier :",main_croupier,total_croupier,"\nVotre jeu :",main_joueur,total_joueur)
            if total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21):
                print("Vous avez gagné !")
            elif total_croupier == total_joueur or (total_croupier > 21 and total_joueur > 21):
                print("Il n'y a aucun gagnant.")
            else:
                print("Vous avez perdu.")
    return None

def blackjack2(bourse):
    mise = int(input("Quelle somme voulez-vous miser ? [nb] "))
    if mise < 0:
        mise = 0
    elif mise > bourse:
        mise = bourse
    main_joueur,main_croupier = tirage(),tirage()
    total_joueur,total_croupier, = total(main_joueur),total(main_croupier)
    print("Le jeu du croupier :",[main_croupier[0],'Carte cachée'],"\nVotre jeu :",main_joueur,total_joueur)
    if total_joueur == 21:
        print("Vous gagnez en obtenant un Blackjack !")
    else:
        suite = input("Que voulez-vous faire ? [O]btenir des cartes/[G]arder ses cartes/[D]oubler la mise et obtenir une carte ")
        if suite.lower() == 'o':
            nb_cartes = int(input("Combien de cartes voulez-vous ? [nb] "))
            main_joueur += tirage(nb_cartes)
            total_joueur = total(main_joueur)
        elif suite.lower() == 'd':
            if mise > bourse:
                mise += bourse
                bourse == 0
            else :
                bourse -= mise
                mise *= 2
        while total_croupier < 17:
            main_croupier += tirage(1)
            total_croupier = total(main_croupier)
        print("Le jeu du croupier :",main_croupier,total_croupier,"\nVotre jeu :",main_joueur,total_joueur)
        if total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21):
            print("Vous avez gagné !")
        elif total_croupier == total_joueur or (total_croupier > 21 and total_joueur > 21):
            print("Il n'y a aucun gagnant.")
        else:
            print("Vous avez perdu.")
    if bourse <= 0:
        print('Vous êtes à sec !')
    rejouer = input("Voulez-vous rejouer ? [Y/N] ")
    if rejouer.lower() == 'y':
        blackjack2(bourse)
    return None

jouer = input("Voulez-vous jouer au Blackjack ? [Y/N] ")
bourse = int(input("Quelle est votre bourse ? [nb] "))
if jouer.lower() == 'y':
    blackjack2(bourse)

