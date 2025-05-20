'''ma_liste =  [12, 32, 23, 15, 8]
print (ma_liste)
 #accede avec indexe l'identifiant d'une liste'''
 
ma_liste = [12, 32, 23, 15, 8]
ma_liste.append(10) # ça ajoute un 10 a la fin de la liste
ma_liste.extend([12,8]) # ajoute l'éléments 12 et 8 à la fin de la liste
ma_liste.insert(1,100) # insère l'élément 100 à l'index 1 (après le 12 car c'est indexe 0)
ma_liste.remove (8) # removes the first 8 appearing in the list
ma_liste.pop(3) #removes l'index 3 seulement alors: 23
print(ma_liste)


#pour la tri d'une liste
nombres = [10, 20, 30, 40, 50]
#         i0   i1  i2  i3  i4
index_30 = nombres.index(30)
print('pour le tri c\'est: ­',index_30) # affiche 2, car 30 est à l’indice 2

#autre opérations
ma_liste = [12, 15, 10, 6, 12, 20]
nb_occurence= ma_liste.count(12) #counts how many times there s the number 12 in the list
print(nb_occurence) 
# to  inverse the the order of the list
ma_liste.reverse()
print(ma_liste)

#operations sur les listes 
une_liste = [1, 2, 3, 4]
une_liste = une_liste + [5, 6, 7] #combnaison de 2 listes ensemble
print(une_liste)
# repetition de la liste
une_liste = [1, 2, 3, 4]*3 
print(une_liste)

#extraction des éléments aux index 2à6 (6 non inclus)
une_liste = [1, 2, 3, 4, 5, 6, 7]
sous_liste = une_liste[2:6]
print (sous_liste)
# extraction de tout les élements sans le dernier
sous_liste = une_liste[:-1]
print(sous_liste) # juste le 7 est effacer 

#diapo 23 pour parcours d'une liste
liste = [1,2,3,4,5]
for i in range(len(liste)):
    print(liste[i])

#diapo 26 creer une nouvelle liste à partir d'une liste
liste = [1,2,3,4,5]
carres = [x*x for x in liste]
print(carres) 

#diapo27 cavec la fonction map
import math

nombres = [1,4,9,16,25]  
racines = list(map(math.sqrt, nombres))
print( 'racines carrées:', racines) # prints the square root of the liste

#  map(foction, nom_liste)
import math # sa c une librairie pour les termes mathematiques

angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2]
sinus = list(map(math.sin,angles))
print ('sinus: ', sinus)

#COMBINAISON DE FORMATAGE DE L'AFFICHAGE DES LISTES
#use pandas. DataFrame
