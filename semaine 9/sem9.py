'''def affichez_message():
    print('yay')
affichez_message()
'''
'''
# Fonction pour calculer la somme des diviseurs stricts
def somme_diviseurs(n):
    diviseurs = []
    for i in range(1, n):
        if n % i == 0:
            diviseurs.append(i)
    return sum(diviseurs)

# Fonction qui vérifie si un nombre est parfait
def parfait(n):
    return somme_diviseurs(n) == n

# Vérification avec les exemples donnés
print("28 est parfait :", parfait(28))    # Doit afficher True
print("106 est parfait :", parfait(106))  # Doit afficher False
'''

def somme_diviseurs(valeur):
     somme = 0
     for i in range(1,valeur):
        if valeur % i == 0:
            somme += i
        return somme
def parfait(valeur):
    if somme_diviseurs(valeur) == valeur:
       return valeur
       
parfait(28)

def somme_diviseurs(valeur):
    somme = 0
    for i in range(1,valeur):
     if valeur % i == 0:
      somme += i
     return somme
def parfait(valeur):
    somme_diviseurs(valeur) == valeur
     return valeur
       
 parfait(28)



total = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total
