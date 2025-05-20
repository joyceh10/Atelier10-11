### Exercice 9 : Génération dynamique d’un tuple
'''- Demandez à l'utilisateur de saisir 5 nombres séparés par un espace.

- Convertissez les entrées en tuple 
et affichez le nombre maximum et la somme des éléments.

cinq_nb = (input("Entrez 5 nombres séparés par un espace: "))
conv = tuple(cinq_nb)
en_tuple = ()
for i in cinq_nb:
    if i != ' ':
     i = int(i)
     en_tuple += (i,)
maximum = max(en_tuple)
print(f"Le nombre maximum est : {maximum}")
somme = (sum(en_tuple))
print(f"La somme des éléments est : {somme}")

donnees_semaine = (
    ("Lundi", 12.3, 18.7, 55),
    ("Mardi", 14.1, 20.2, 60),
    ("Mercredi", 13.5, 19.8, 52),
    ("Jeudi", 11.8, 17.9, 58),
    ("Vendredi", 15.2, 21.4, 65),
    ("Samedi", 16.0, 22.5, 70),
    ("Dimanche", 14.5, 20.1, 63),
)
# Affichage lisible des données météo
print(" Données météo de la semaine :\n")

for jour, temp_min, temp_max, humidite in donnees_semaine:
    print(f"{jour} : Temp. min = {temp_min}°C | Temp. max = {temp_max}°C | Humidité = {humidite}%")'''

donnees_semaine = (
    ("Lundi", 12.3, 18.7, 55),
    ("Mardi", 14.1, 20.2, 60),
    ("Mercredi", 13.5, 19.8, 52),
    ("Jeudi", 11.8, 17.9, 58),
    ("Vendredi", 15.2, 21.4, 65),
    ("Samedi", 16.0, 22.5, 70),
    ("Dimanche", 14.5, 20.1, 63),
)
print("Données de la semaine:")
for jour, min, max, humidite in donnees_semaine:
 print(f"{jour}:  T˚ min {min} ˚C , T˚ max {max}˚C , Taux d'humidité {humidite}")
print(" ")
minTotal = 0
maxTotal = 0
for jour, min, max, humidite in donnees_semaine: #pour trouver les moyennes
 minTotal += min
 maxTotal += max
minTotal = round(minTotal / len(donnees_semaine),2)
maxTotal = round(maxTotal / len(donnees_semaine),2)
print(f"La moyenne minimale de la semaine est {minTotal}˚C")
print(f"La moyenne maximale de la semaine est {maxTotal}˚C") 
print()
chaud_journee = ""
temp_chaud = 0
for jour, min, maxi, humidite in donnees_semaine: #jour le plus chaud
 while max >= temp_chaud:
  chaud_journee = jour
print(f"Le jour le plus chaud: {chaud_journee}")

