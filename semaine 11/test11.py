'''i = 1
while i < 13 :
    prod = 9 * i 
    print(f' 9 X {i} = {prod}')
    i += 1

liste = [2, 9, 3,5]
print(liste) # [2, 9, 3, 5]
tuple(liste) # (2, 9, 3, 5)

cinq_nb = (input("Entrez 5 nombres séparés par un espace: "))
conv = tuple(cinq_nb)
en_tuple = ()
for i in conv:
    if i != ' ':
     i = int(i)
     en_tuple += (i,)
maximum = max(en_tuple)
somme = sum(en_tuple)
print(f"Le nombre maximum est  {maximum}")
print(f"La somme est {somme}")


donnees_semaine = (
    ("Lundi", 12.3, 18.7, 55),
    ("Mardi", 14.1, 20.2, 60),
    ("Mercredi", 13.5, 19.8, 52),
    ("Jeudi", 11.8, 17.9, 58),
    ("Vendredi", 15.2, 21.4, 65),
    ("Samedi", 16.0, 22.5, 70),
    ("Dimanche", 14.5, 20.1, 63),
)

# Initialisation
temp_max = donnees_semaine[0][2]
jour_plus_chaud = donnees_semaine[0][0]

# Boucle pour comparer chaque jour
for jour, t_min, t_max, humidite in donnees_semaine:
    if t_max > temp_max:
        temp_max = t_max
        jour_plus_chaud = jour

print(f"La journée la plus chaude est {jour_plus_chaud} avec {temp_max}°C.")'''

lst= [2, 1, 6, 7]
tuple1= tuple(lst)
print(tuple1)
lst_encore = list(tuple1)
lst_encore.append(10)
print(lst_encore)
