#a=20
#print ('voici la valeur:' , a )

# Type int (entier)
nombre_entier = 42
print(nombre_entier, "est de type", type(nombre_entier)) 
# Affiche : 42 est de type <class 'int'>
# Type float (flottant)
nombre_flottant = 67.8
print(nombre_flottant, "est de type", type(nombre_flottant)) 
# Affiche : 67.8 est de type <class 'float'>
# Type bool (booléen)
valeur_booleenne = True
print(valeur_booleenne, "est de type", type(valeur_booleenne)) 
# Affiche : True est de type <class 'bool'>
# Type complex (complexe)
nombre_complexe = 1 + 2j
print(nombre_complexe, "est de type", type(nombre_complexe)) 
# Affiche : (1+2j) est de type <class 'complex'>
# Changement dynamique de type
variable = 10 # int
print(variable, "est de type", type(variable)) 
# Affiche : 10 est de type <class 'int'>
variable = 3.14 # float
print(variable, "est de type", type(variable)) 
# Affiche : 10.5 est de type <class 'float'>
variable = "Bonjour" # str (chaîne de caractères)
print(variable, "est de type", type(variable))