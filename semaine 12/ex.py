'''nb_personne = int(input("Combien y a t il de personnes? "))
prix = []
for i in range(1,nb_personne + 1):
    age = int(input(f"Quel est l'age de la personne {i}? "))
    if age < 4:
        prix.append(0)
    elif 4 <= age <= 10:
        prix.append(6)
    elif 11 <= age <= 17:
        prix.append(10)
    elif 18 <= age <= 64:
        prix.append(18)
    else:
        prix.append(12)
    total = sum(prix)
print(total)'''



'''
nb_personne = int(input("Combien y a t il de personnes? "))
prix = 0
for i in range(1,nb_personne + 1):
    age = int(input(f"Quel est l'age de la personne {i}? "))
    if age < 4:
        prix+= 0
    elif 4 <= age <= 10:
        prix += 6
    elif 11 <= age <= 17:
        prix += 10
    elif 18 <= age <= 64:
        prix += 18
    else:
        prix += 12
    
print(prix)''' 
import math
vecteurs = ((3,4), (1,-2),(-5,2), (0,0), (2,3))
normes = [math.sqrt(v[0]**2 + v[1]**2) for v in vecteurs] 
for v in vecteurs:
    formule = math.sqrt(v[0]**2 + v[1]**2)
    if formule == max(normes):
        print(f"Le vecteur avec la plus grande norme est {v}")
    elif formule == min(normes):
        print(f"Le vecteur avec la plus petite norme est {v}")
    

