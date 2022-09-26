import random as rd

"""
Règles du Blackjack :
    Dans notre version le Blackjack est avec un joueur contre le croupier.
    A chaque carte est associé un nombre de points, pour celles numérotées de 2 à 9, elles ont le même nombre de points que leur valeur, pour le 10, le
    Valet, la Dame et le Roi, elles valent 10 points, et l'As prend soit 1 ou 11 points en fonction de si cela aide le joueur ou pas.
    La partie se déroule en 1 ou 2 tours.
    Une partie commence par une 1ère distribution de deux cartes pour le joueur et une carte face vers le haut et une autre face vers le bas pour le
    croupier. Si le joueur obtient un Blackjack (un as et une carte valant 10) la partie s'arrête à ce moment par la victoire du joueur.
    Ensuite, pour le 2ème tour le joueur choisi entre obtenir des cartes supplémentaires ou garder ses cartes, puis le croupier récupère des cartes jusqu'à
    ce que le total de ces cartes soit supérieur à 17.
    Le joueur gagne si le total des points de ses cartes est supérieur à celui du croupier ou que les points du croupier dépassent 21 et qu'il ne dépasse
    pas 21, ou alors il n'y a pas de gagnant car le total de la main du joueur est égal à celui du croupier ou que les deux dépasse 21 et enfin sinon le
    joueur a perdu.
"""

#listes utilisées pour faire les tirages de cartes
liste_valeurs = ['A','2','3','4','5','6','7','8','9','10','V','D','R']
liste_signes = ['♥','♦','♣','♠']

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
        if valeur == 'A': #associe un nombre de point en fonction de la valeur de la carte
            point = 11
        elif valeur in '23456789':
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
            if carte[0][0]=='A' and total > 21: #si le total est supérieur à 21 et que la carte est un as, remplace la valeur de l'as par 1 et actualise la valeur du total
                carte[1] = 1
                total -= 10
            elif total <= 21: #et si le total est inférieur ou égal à 21 la boucle se termine
                break
    return total



def blackjack():
    """
    Lance une partie de Blackjack.
    """
    jouer = input("Voulez-vous jouer au Blackjack ? [Y/N] ")
    if jouer.lower() == 'y':
        main_joueur,main_croupier = tirage(),tirage() #fait 2 tirage de 2 cartes, pour le joueur et le croupier
        total_joueur,total_croupier, = total(main_joueur),total(main_croupier) #fait les totaux des mains du joueur et du croupier

        print("\n1er tour :") #affiche les mains en cachant la 2eme carte du croupier et le total de la main du joueur pour le 1er tour
        print("La main du croupier :",[main_croupier[0],'Carte cachée'],"\nVotre main :",main_joueur,"\n Total de vos cartes :",total_joueur,'\n')

        if total_joueur == 21:
            print("Vous gagnez en obtenant un Blackjack !") #victoire en ayant 21 points dès le premier tirage

        else:
            suite = input("Voulez-vous des cartes supplémentaires ? [Y/N] ") #demande si le joueur veut des cartes supplémentaires
            if suite.lower() == 'y':
                nb_cartes = int(input("Combien de cartes voulez-vous ? [nb] ")) #demande le nombre de cartes supplémentaires voulu par le joueur et les rajoute à la main, puis recalcule le total
                main_joueur += tirage(nb_cartes)
                total_joueur = total(main_joueur)

            while total_croupier < 17: #rajoute des cartes à la main du croupier jusqu'à ce que le total dépasse ou égalise 17
                main_croupier += tirage(1)
                total_croupier = total(main_croupier)

            print("\n2eme tour :") #affiche les mains et les totaux du croupier et du joueur pour la fin du jeu
            print("La main du croupier :",main_croupier,"\n Total des cartes du croupier :",total_croupier,"\nVotre main :",main_joueur,"\n Total de vos cartes :",total_joueur)

            if total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21): #conditions pour gagner
                print("\nVous avez gagné !")
            elif total_croupier == total_joueur or (total_croupier > 21 and total_joueur > 21): #conditions si il n'y a pas de gagnant
                print("\nIl n'y a aucun gagnant.")
            else: #sinon défaite
                print("\nVous avez perdu.")
    return None



def affichage(main,cache=False):
    """
    Renvoie une chaine de caractère pour afficher les cartes dans la console.
    """
    lignes,visuel = [],""
    for k in range(len(main)): #ajoute les cartes ligne par ligne dans la liste lignes
        carte = main[k]
        valeur,signe = carte[0][0],carte[0][1]

        lignes.append("╔═══════════╗ ") #1ere ligne

        if k == 1 and cache: #cache la 2eme carte si cache=True
            for _ in range(4):
                lignes.append("║* * * * * *║ ")
                lignes.append("║ * * * * * ║ ")

        else:
            if valeur == '10': #2eme ligne
                lignes.append("║10         ║ ")
            else:
                lignes.append("║"+valeur+"          ║ ")

            if valeur == '8' or valeur == '10': #3eme ligne
                lignes.append("║"+signe+"  "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║"+signe+"          ║ ")

            if valeur in '23' or valeur == '10' : #4eme ligne
                lignes.append("║     "+signe+"     ║ ")
            elif valeur in '45679':
                lignes.append("║   "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║           ║ ")

            if valeur in '89' or valeur == '10': #5eme ligne
                lignes.append("║   "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║           ║ ")

            if valeur in 'A359': #6eme ligne
                lignes.append("║     "+signe+"     ║ ")
            elif valeur in '678' or valeur == '10':
                lignes.append("║   "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║           ║ ")

            if valeur == '7' or valeur == '10' : #7eme ligne
                lignes.append("║     "+signe+"     ║ ")
            elif valeur == '9':
                lignes.append("║   "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║           ║ ")

            if valeur in '23': #8eme ligne
                lignes.append("║     "+signe+"     ║ ")
            elif valeur in '456789' or valeur == '10':
                lignes.append("║   "+signe+"   "+signe+"   ║ ")
            else:
                lignes.append("║           ║ ")

            lignes.append("║           ║ ") #9eme ligne

        lignes.append("╚═══════════╝ ") #10eme ligne

    for i in range(10): #met en ordre les lignes des cartes pour les renvoyer dans une chaine de caractère
        for j in range(i,len(lignes),10):
            visuel += lignes[j]
        visuel += '\n'

    return visuel



def blackjack_v3(bourse):
    """
    Lance une partie de Blackjack avec le visuel des cartes dans la console (agrandir la taille de la console au préalable).
    """
    main_joueur,main_croupier = tirage(),tirage() #fait 2 tirage de 2 cartes, pour le joueur et le croupier
    total_joueur,total_croupier, = total(main_joueur),total(main_croupier) #fait les totaux des mains du joueur et du croupier

    mise = int(input("Quelle somme voulez-vous miser ? [nb] "))
    if mise < 0:
        mise = 0
    elif mise > bourse:
        mise = bourse
    bourse -= mise


    print("\n1er tour :\n") #affiche les mains en cachant la 2eme carte du croupier et le total de la main du joueur pour le 1er tour
    print("La main du croupier :")
    print(affichage(main_croupier,True))
    print("Votre main :")
    print(affichage(main_joueur),"Total de vos cartes :",total_joueur,'\n',"Bourse : ",bourse,"\t Mise : ",mise,'\n')

    if total_joueur == 21:
        bourse += mise*1.5
        print("Vous gagnez en obtenant un Blackjack !") #victoire en ayant 21 points dès le premier tirage
    else:
        suite = input("Que voulez-vous faire ? [O]btenir des cartes/[G]arder ses cartes/[D]oubler la mise et obtenir une carte ") #demande si le joueur veut des cartes supplémentaires
        if suite.lower() == 'o':
            nb_cartes = int(input("Combien de cartes voulez-vous ? [nb] ")) #demande le nombre de cartes voulu par le joueur et les rajoute à la main, puis recalcule le total
            main_joueur += tirage(nb_cartes)
            total_joueur = total(main_joueur)

        elif suite.lower() == 'd':
            if mise > bourse:
                mise += bourse
                bourse == 0
            else :
                bourse -= mise
                mise *= 2
            main_joueur += tirage(1)
            total_joueur = total(main_joueur)

        while total_croupier < 17: #rajoute des cartes à la main du croupier jusqu'à ce que le total dépasse ou égalise 17
            main_croupier += tirage(1)
            total_croupier = total(main_croupier)

        print("\n2eme tour :\n") #affiche les mains et les totaux du croupier et du joueur pour la fin du jeu
        print("La main du croupier :")
        print(affichage(main_croupier),"Total des cartes du croupier :",total_croupier,'\n')
        print("Votre main :")
        print(affichage(main_joueur),"Total de vos cartes :",total_joueur,'\n',"Bourse : ",bourse,"\t Mise : ",None,'\n')
        if total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21): #conditions pour gagner
            bourse += mise*2
            print("Vous avez gagné !")
        elif total_croupier == total_joueur or (total_croupier > 21 and total_joueur > 21): #conditions si il n'y a pas de gagnant
            bourse += mise
            print("Il n'y a aucun gagnant.")
        else: #sinon défaite
            print("Vous avez perdu.")
    if bourse <= 0:
        print('Vous êtes à sec !')
    rejouer = input("Voulez-vous rejouer ? [Y/N] ")
    if rejouer.lower() == 'y':
        blackjack_v3(bourse)
    return None

jouer = input("Voulez-vous jouer au Blackjack ? [Y/N] ")
if jouer.lower() == 'y':
    bourse = int(input("Quelle est votre bourse ? [nb] "))
    blackjack_v3(bourse)
