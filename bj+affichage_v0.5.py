import random as rd

#listes utilisées pour faire les tirages de cartes
liste_valeurs = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
liste_signes = ['♥','♦','♣','♠']

#polices utilisées pour l'affichage
pol_c1 = ('┌','┐','─','└','┘','│','┬','┴','├','┤','┼')
pol1 = ('╔','╗','═','╚','╝','║','╦','╩','╠','╣','╬')
pol2 = ('/',"'\'",'~',"'\'",'/','!','~','~','}','{','+')

"""
carte = une liste sous la forme [(valeur,signe),point]
main = une liste de cartes sous la forme [carte,carte,...]
"""

def tirage(nb=2):
    """
    Renvoie une main de nb carte tirée aléatoirement.
    """
    main = []
    for _ in range(nb):
        valeur = rd.choice(liste_valeurs) #donne une valeur aléatoire
        if valeur == '1': #associe un nombre de point en fonction de la valeur de la carte
            point = 11
        elif valeur in '2,3,4,5,6,7,8,9':
            point = int(valeur)
        else:
            point = 10
        main.append([(valeur,rd.choice(liste_signes)),point]) #crée une carte en associant la valeur avec un signe tirée aléatoirement(le signe n'a pas d'utilité à part esthétique) et les points et ajoute cette carte à la main
    return main

def total(main):
    """
    Renvoie le total des valeurs des cartes de main et change la valeur des as en 1 en fonction de si le total dépasse 21.
    """
    total = 0
    for carte in main: #fait le total des valeurs des cartes de main avec 11 comme valeur de l'as
        total += carte[1]
    if total > 21:
        for carte in main:
            if carte[0][0]=='1' and total > 21: #si le total est supérieur à 21 et que la carte est un as, remplace la valeur de l'as par 1 et actualise la valeur du total
                carte[1] = 1
                total -= 10
            elif total <= 21: #et si le total est inférieur ou égal à 21 la boucle se termine
                break
    return total

def newframe (size, police_frame, police_cards, state_of_game, main_joueur, main_croupier, total_joueur, total_croupier):
    """
    affiche l'image du jeu
    """
    if police_frame == 1:
        pol_f = pol1
    elif police == 2:
        pol_f = pol2
    else:
        print('error_police')

    if police_cards == 1:
        pol_c = pol_c1
    else:
        print('error_police')

    #base values
    Width = 100
    Height = 100
    frame =''
    frame += pol1[0] + pol1[2]*(Width-2) + pol1[1] + '\n'

    if size == '200:100':
        Width = 200
        Height = 100

    if state_of_game==0:
        cardsWidth = Width//5
        cardsHeight = Height//5

        height_emptiness = Height-2 - cardsHeight*2
        croupier_width_emptiness = Width-2 - cardsWidth*len(main_croupier)
        joueur_width_emptiness = Height-2 - cardsWidth*len(main_joueur)

        frame =''
        frame += pol1[0] + pol1[2]*(Width-2) + pol1[1] + '\n'

        #Carte(s) du croupier
        for i in range(cardsHeight):
            frame += pol1[5] + ' ' * croupier_width_emptiness + pol_c[5]  + ' ' * cardsWidth + pol_c[5]  + ' ' * croupier_width_emptiness + pol1[5] + '\n'
        frame += pol1[5] + ' ' * croupier_width_emptiness + pol_c[3]  + pol_c[2] * cardsWidth + pol_c[4]  + ' ' * croupier_width_emptiness + pol1[5] + '\n'

        #Espace entre les mains
        for i in range(height_emptiness):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

        #Carte(s) du joueur
        frame += pol1[5] + ' ' * joueur_width_emptiness + pol_c[0]  + pol_c[2] * cardsWidth + pol_c[1]  + ' ' * joueur_width_emptiness + pol1[5] + '\n'
        for i in range(cardsHeight):
            frame += pol1[5] + ' ' * joueur_width_emptiness + pol_c[5]  + ' ' * cardsWidth + pol_c[5]  + ' ' * joueur_width_emptiness + pol1[5] + '\n'

    elif state_of_game==1:
        for _ in range(Height-2):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

    elif state_of_game==2:
        for _ in range(Height-2):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

    elif state_of_game==3:
        for _ in range(Height-2):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

    frame += pol1[3] + pol1[2] * (Width-2) + pol1[4]

    return frame

def blackjack():
    """
    Lance une partie de Blackjack.
    """
    jouer = input("Voulez-vous jouer au Blackjack ? [Y/N] ")
    if jouer.lower() == 'y':
        main_joueur,main_croupier = tirage(),tirage() #fait 2 tirage de 2 cartes, pour le joueur et le croupier
        total_joueur,total_croupier, = total(main_joueur),total(main_croupier) #fait les totaux des mains du joueur et du croupier
        if total_joueur == 21:

            print(newframe('200:100',1,1,2,main_joueur,main_croupier,total_joueur,total_croupier)) #affiche la victoire en ayant 21 points dès le premier tirage
        else:
            print(newframe('200:100',1,1,0,main_joueur,main_croupier,total_joueur,total_croupier)) #affiche les mains et le total de la main du joueur en cachant la 2eme carte du croupier

            suite = input("Voulez-vous des cartes supplémentaires ? [Y/N] ")
            if suite.lower() == 'y':
                nb_cartes = int(input("Combien de cartes voulez-vous ? [nb] ")) #demande le nombre de cartes supplémentaires voulu par le joueur et les rajoute à la main, puis recalcule le total
                main_joueur += tirage(nb_cartes)
                total_joueur = total(main_joueur)
            while total_croupier < 17: #rajoute des cartes à la main du croupier jusqu'à ce que le total dépasse ou égalise 17
                main_croupier += tirage(1)
                total_croupier = total(main_croupier)

            print(newframe('200:100',1,1,0,main_joueur,main_croupier,total_joueur,total_croupier)) #affiche les mains et les totaux du croupier et du joueur

            if total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21): #conditions pour gagner

                print(newframe('200:100',1,1,1,main_joueur,main_croupier,total_joueur,total_croupier))

            elif total_croupier == total_joueur or (total_croupier > 21 and total_joueur > 21): #conditions si il n'y a pas de gagnant

                print(newframe('200:100',1,1,3,main_joueur,main_croupier,total_joueur,total_croupier))

            else: #sinon défaite

                print(newframe('200:100',1,1,2,main_joueur,main_croupier,total_joueur,total_croupier))
    return None
