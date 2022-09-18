pol_c1 = ('┌','┐','─','└','┘','│','┬','┴','├','┤','┼')
pol1 = ('╔','╗','═','╚','╝','║','╦','╩','╠','╣','╬')
pol2 = ('/',"'\'",'~',"'\'",'/','!','~','~','}','{','+')

main_croupier = [[]]
main_joueur_01 = [[]]


def newframe (Width, Height, police_frame, police_cards):

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


    frame =''
    frame += pol1[0] + pol1[2]*(Width-2) + pol1[1] + '\n'

    if main_croupier and main_joueur_01:

        cardsHeight = (Height)//4
        cardsWidth = (Width)//6

        height_emptiness = Height - cardsHeight*2
        croupier_width_emptiness = (Width-2 - cardsWidth*len(main_croupier))//2
        joueur_width_emptiness = (Width-2 - cardsWidth*len(main_joueur_01))//2

        ##Carte(s) du croupier
        for i in range(cardsHeight):
            frame += pol1[5] + ' ' * croupier_width_emptiness + pol_c[5]  + ' ' * cardsWidth + pol_c[5]  + ' ' * croupier_width_emptiness + pol1[5] + '\n'
        frame += pol1[5] + ' ' * croupier_width_emptiness + pol_c[3]  + pol_c[2] * cardsWidth + pol_c[4]  + ' ' * croupier_width_emptiness + pol1[5] + '\n'

        ##Espace entre les mains
        for i in range(height_emptiness):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

        ##Carte(s) du joueur
        frame += pol1[5] + ' ' * joueur_width_emptiness + pol_c[0]  + pol_c[2] * cardsWidth + pol_c[1]  + ' ' * joueur_width_emptiness + pol1[5] + '\n'
        for i in range(cardsHeight):
            frame += pol1[5] + ' ' * joueur_width_emptiness + pol_c[5]  + ' ' * cardsWidth + pol_c[5]  + ' ' * joueur_width_emptiness + pol1[5] + '\n'


    else:
        for i in range(Height-2):
            frame += pol1[5] + ' ' * (Width-2) + pol1[5] + '\n'

    frame += pol1[3] + pol1[2] * (Width-2) + pol1[4]

    return frame





print(newframe(200,50,1,1))
