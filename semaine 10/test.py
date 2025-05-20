"""import numpy as np

# Data for pollutants (Mercure, Nitrates, Pesticides)
mercure = [0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065]
nitrates = [2.5, 2.7, 3.0, 3.2, 3.5, 3.8, 4.0, 4.3, 4.6, 5.0]
pesticides = [0.10, 0.12, 0.14, 0.15, 0.17, 0.19, 0.20, 0.22, 0.24, 0.26]

# Calculating the statistics using NumPy
def calculate_statistics(data):
    mean = np.mean(data)
    range_ = np.ptp(data)  # Range is the peak-to-peak value (max - min)
    std_dev = np.std(data)
    variance = np.var(data)
    
    return mean, range_, std_dev, variance

# For Mercure
mercure_stats = calculate_statistics(mercure)
# For Nitrates
nitrates_stats = calculate_statistics(nitrates)
# For Pesticides
pesticides_stats = calculate_statistics(pesticides)

# Display the results
pollutants = ['Mercure (ppm)', 'Nitrates (ppm)', 'Pesticides (ppm)']
stats = [mercure_stats, nitrates_stats, pesticides_stats]

for pollutant, stat in zip(pollutants, stats):
    print(f"\n{pollutant}:")
    print(f"  Moyenne: {stat[0]:.4f}")
    print(f"  Étendue: {stat[1]:.4f}")
    print(f"  Écart-type: {stat[2]:.4f}")
    print(f"  Variance: {stat[3]:.4f}")


polluants = {"mercure": cmercure, "nitrates": cnitrates, "pesticides": cpesticides}
df = pd.DataFrame(polluants)
statistiques = {}
for p in polluants:
    statistiques[p] = {"moyenne": df[p].mean(), "étendue": df[p].max()-df[p].min() , "écart type": df[p].std,
                     "variance": df[p].var()}
    

for p, values in statistiques.items():
    print(p, ":")
    for statistiques, value in values.items():
        print(statistiques, f": {value}")"""

'''import pandas as pd
#évolution d'energie dans ses scénarios
#calcul énergie cinetique
so_ec= []
sc_ec = []
annees = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
temp = [15.0, 15.7, 15.7, 16.1, 16.6, 17.2, 17.8, 18.3, 18.9, 19.5]

for i in range(len(temp)):
    temp_K = 16 + 273.15
    E_c = (3/2) * kB * temp_K
    so_ec.append(E_c)

for n in range(len(temp)):
    temp[n] += 1.5 
    temp_K = temp[n] + 273.15
    E_c = (3/2) * kB * temp_K
    sc_ec.append(E_c)
    

print("Évolution énergie cinetique:")
data = {"années":annees, "scénario optimiste" : so_ec, "scénario catastrophique": sc_ec}
df = pd.DataFrame(data)
print(df)'''

import math
import numpy as np
def taux_de_croissance(pmax,pt, p0, t): #r
    return (-1/t) *  np.log(((pmax-pt)/pt)*(p0/(pmax-p0)))
r = taux_de_croissance(50000, 28000, 25000, 9) #pour 2028 t=9
print(r)
import math
def formule_croisssance_logistique(pmax, p0, r, t):
  return pmax / (1 + ((pmax - p0) / p0) * math.e ** (-r * t))
resultat = formule_croisssance_logistique(50000, 25000, r,10)
print(resultat)