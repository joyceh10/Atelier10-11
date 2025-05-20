# Ce programme permet de lire 10 notes au clavier et de calculer leur moyenne.
""""""
'''
somme = 0
for i in range(10):
 note = float(input(f"Entrez la note {i+1} : "))
 somme += note
moyenne = somme / 10
print("La moyenne des notes est :", moyenne)
'''
'''

nombre = int(input("Entrez un nombre : "))
somme = 0
for i in range(1, nombre + 1):
 somme += i
print("La somme calculée est :", somme)

n = int(input("Entrez un nombre: "))
for i in range ( 0, n+1):
    print("*" * (2 * i - 1))

nombre = int(input("Entrez un nombre : "))
somme = 0
for i in range(1, nombre + 1):
 somme += i
print ("La somme calculée est :", somme)
   

#ex5:
n = int(input("saisir un nombre: "))
produit = 1
for p in range (1, n+1):
    produit *= p
print("n! : ", produit) 


n = int(input("Entrez un nombre entre 1 et 10: "))
while 1 <= n <= 10:
    print (n)
    n = int(input("Entrez un nombre entre 1 et 10: "))
    ''' 
'''''
#ex 8
a = int(input("Entrez le premier nombre: " ))
b = int(input("Entrez le deuxième nombre: " ))
pgcd = a % b
while pgcd !=0 :
    a = b
    b = pgcd
    pgcd = a % b
print ("Le PGCD est", b)

#ex6 test 
n = int(input("entrez un chiffre: "))
for i in range ( 0, n +1):
    print(" "* (n-i),'*'* ((2*i)+1))
 '''''

'''
for i in range(5):  # Boucle de 1er niveau
    barre = " "
    for j in range(i+1): # Boucle de 2e niveau
        barre += "# "
    print(barre)

  n = int(input("entrez un nombre: "))
for i in range(5):
   b = " "  #try this after
   for m in range(i+1):
      b += "*"
      print (b)


#ex 9
chaine = input("Saisir une chaîne de caractères: ")
while chaine != "stop":
    chaine = input("Saisir une chaîne de caractères: ")
print ("stop")'''

#ex 10
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
print ("C'est vraiment moi!!")
