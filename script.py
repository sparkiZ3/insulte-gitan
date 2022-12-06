import random
fichier = open("data.txt", "r") #ouverture du fichier de donnée
masculin_recup=fichier.readline() #on recupere la premiere ligne qui correspond aux mots masculins
feminin_recup=fichier.readline() #on recupere la seconde ligne qui correspond aux mots féminin
masculin=masculin_recup.split() #on met les mots dans une liste avec la fonction split()
feminin=feminin_recup.split()
if random.randint(1, 2)==1: #choix aléatoire féminin ou masculin
    print("le "+random.choice(masculin)+" de tes morts") #on affiche la phrase au masculin
else:
    print("la "+random.choice(feminin)+" de tes morts") #on affiche la phrase au féminin
fichier.close() #on ferme le fichier