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
