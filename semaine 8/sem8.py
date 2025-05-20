'''mots = ["Bonjour", "tout", "le", "monde"]
phrase = " ".join(mots) # "Bonjour tout le monde"
print(phrase)

fin = "Bonjour".endswith("our")
print(fin)'''

'''chaine = input('enter a word: ')
chaine = chaine.strip().lower()
if chaine==chaine[::-1]:
    print('this is a palindrome')
else:
    print(chaine, 'n\'est pas un palindrome')'''

seq_adn = 'CGTATGCAGTTACG'
'''i = input('entrez une base de nucleotide (A,T,C OU G):')
compte = 0
if i in seq_adn == 'A C T G':
     compte += 1
     print(compte)'''

for i in seq_adn:
    if i == 'A':
        print('T')
    if i == ('T'):
        print ('A')
    if i == ('C'):
        print('G')
    if i == ('G'):
        print ('C')

'''while True:
    i = input('entrez une base de nucleotide (A,T,C OU G):')
    if i in ('A T C G') and len(i)== 1:
        break
    else:
     print('incorrecte, entrez seulement A,T,C OU G')
compte = seq_adn.count(i)
print(f'il y a {compte} {i} dans cette sequence d\' ADN')'''


base = input('Entrez un nucléotide: ')
compte = 0
for i in seq_adn:
    if i in  base :
        compte += 1
print(f'il y a {compte} {base} dans cette séquence')


    

