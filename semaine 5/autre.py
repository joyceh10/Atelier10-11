'''''
nombre1= 20
nombre2= 30
somme = None
print('voici la valeur de somme au depart', type(somme))
'''
"""" ex 9
longueur = int(input( 'Entrez la longueur du rectangle: ' ))
largeur = int(input( 'Entrez la largeur du rectangle: '))
#calcul de l'aire et le périmetre
aire = longueur * largeur
perimetre= 2*longueur + 2*largeur 
# affichage de l'aire et du périmètre
print ('Voici l\'aire du rectangle:', aire )
print ('Voici le périmètre du rectangle', perimetre)

ex 10
r = int(input('Entrez le rayon du cercle: '))
pi = 3.14159
# calcul de l'aire et du périmètre du cercle
aire = pi * r**2
perimetre = 2 * pi * r
print ('L\'aire du cercle est: ', aire)
print ('Le périmètre du cercle est: ', perimetre)

temperature = int(input('La température en degré Fahrenheit: '))
conversion = (temperature-32)* (5/9)
print('La température en degré Celsius est: ', conversion, '˚C')

n1 = int(input(' entrez la première note: '))
n2 = int(input(' entrez la deuxième note: '))
n3 = int(input(' entrez la troisième note: '))
moyenne = (n1+n2+n3)/ 3
print(' Votre moyenne est: ', moyenne)

nb = int(input('Entrez un nombre '))
if nb == 10:
    print (' Le nombre est 10 ')
 
nb = int(input('Entrez un numéro: '))
if nb< 10:
    print('Le nombre est inférieur à 10')
else:
    print( ' Le nombre est supérieur ou égal à 10') 
 """ 
n = input(" Quel est votre nom? ")
p = input(" Quel est votre prénom? ") 
nom = "Hidalgo"
prenom = "Joyce"
while n != nom and p != prenom :
 print ("Nom et prénom ne correspondent pas!")
 n = input(" Quel est votre nom? ")
 p = input(" Quel est votre prénom? ") 
while n != nom and p == prenom:
  print ("Nom ne correspond pas!")
  n = input(" Quel est votre nom? ")
while n== nom and p != prenom:
   print ("Prénom ne correspond pas!")
   p = input(" Quel est votre prénom? ")
print (f"C'est vraiment moi!! {p} {n}")