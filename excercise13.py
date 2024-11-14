import numpy as np
from math import log10 

# 1. Variante mit math
x = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]

x_log10 = [log10(k) for k in x]

print(x_log10) # Erstellt eine normal Liste


# 2. Variante mit Numpy

x_log10_array = np.log10(x)

print(x_log10_array) # Erstellt einen Numpy Array wichtiger Unterschied zur Liste