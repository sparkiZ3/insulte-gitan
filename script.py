import random
fichier = open("data.txt", "r") #ouverture du fichier de donnée
masculin=fichier.readline().split() #on met les mots dans une liste avec la fonction split()
feminin=fichier.readline().split()
if random.randint(1, 2)==1: #choix aléatoire féminin ou masculin
    print("le "+random.choice(masculin)+" de tes morts") #on affiche la phrase au masculin
else:
    print("la "+random.choice(feminin)+" de tes morts") #on affiche la phrase au féminin
fichier.close() #on ferme le fichier
