'''nb_entier = int(input("Entrez un nombre strictement positif: "))
if nb_entier > 0:
    somme = 0
    for nb in range(1,nb_entier+1):
        calcul = nb**2
        somme += calcul
    print(somme)
else:
    nb_entier= int(input('Incorrect, entrez un nombre strictement positif: '))
    somme = 0
    for nb in range(1,nb_entier+1):
        calcul = nb**2
        somme += calcul
    print(somme)

chaine = input("Saisir une chaîne de caractères: ")
while chaine != "stop":
    chaine = input("Saisir une chaîne de caractères: ")
print (chaine)'''

n = int(input("Entrez un nombre entier pour calculer son factoriel : "))
factoriel = 1
for i in range(1, n + 1):
    factoriel *= i
print('Le',str(n)+"!=", factoriel )

